"""Additional diagnostics and the offline dashboard from validated order data."""
import json
import numpy as np
import pandas as pd
from plotly.offline import get_plotlyjs

def build_portfolio(root, clean, results):
    detail=results['07_product_discount_detail'].set_index(['product','discount_band']).sort_index()
    expected=clean.groupby(['product','discount_band']).agg(orders=('order_id','count'),revenue=('revenue','sum'),profit=('profit','sum'))
    np.testing.assert_allclose(detail[['orders','revenue','profit']],expected)
    np.testing.assert_allclose(detail['margin_pct'],100*expected.profit/expected.revenue)
    first=clean.groupby('customer_id').order_date.min()
    eligible=first[first+pd.Timedelta(days=90)<=pd.Timestamp('2025-12-31')]
    follow=clean.merge(eligible.rename('first_date'),left_on='customer_id',right_index=True)
    follow['repeated']=(follow.order_date>follow.first_date)&(follow.order_date<=follow.first_date+pd.Timedelta(days=90))
    people=follow.groupby('customer_id').agg(first_date=('first_date','first'),repeated=('repeated','max'))
    people['first_purchase_month']=people.first_date.dt.strftime('%Y-%m')
    expected=people.groupby('first_purchase_month').agg(eligible_customers=('repeated','size'),repeat_customers=('repeated','sum'))
    actual=results['08_repeat_within_90_days'].set_index('first_purchase_month').sort_index()
    np.testing.assert_allclose(actual[['eligible_customers','repeat_customers']],expected)
    np.testing.assert_allclose(actual.repeat_90d_pct,100*expected.repeat_customers/expected.eligible_customers)
    high=clean[clean.discount_band.eq('High (>10%)')]
    report=f'''# Business case: prioritize discount economics

## Decision and evidence
Investigate discount economics before recommending more sales volume.
The high-discount band has **{100*high.profit.sum()/high.revenue.sum():.2f}% contribution margin**
across {len(high):,} orders in this synthetic case.

| Finding | Interpretation | Proposed next step |
|---|---|---|
| {int(clean.profit.lt(0).sum()):,} loss-making orders | Positive product totals can hide weak transactions | Review price and shipping costs at order level |
| Negative margin in the high-discount band | Overall averages may hide product mix | Compare bands within products using SQL 07 |
| {people.repeated.mean():.2%} repeat within 90 days | Comparable follow-up for {len(people):,} eligible customers | Design a second-purchase experiment |
| {len(first)-len(people):,} customers excluded from 90-day analysis | Late entrants have insufficient follow-up | Do not count these customers as non-repeaters |

## Proposed experiment
Randomize eligible customers within product/category strata to the current offer
or a lower-discount offer. Measure contribution profit per eligible customer,
including non-buyers in the denominator. Track conversion and refunds as guardrails.
Predefine a sample-size calculation using real baseline data before launching.

No profit uplift is forecast. A fixed-volume repricing scenario ignores demand
response. Generated discounts and quantities cannot establish real-world effects.

## Measurement boundaries
The 90-day analysis requires first purchase + 90 days <= 31 December 2025.
A repeat occurs strictly after the first purchase date and within 90 days.
Same-day extra orders do not count. Dashboard frequency instead means at least
two orders within selected filters. Neither measure is cohort retention.

## Supporting outputs
- [Product-discount comparison](07_product_discount_detail.csv)
- [90-day eligible follow-up](08_repeat_within_90_days.csv)
- [Five-question summary](executive_summary.md)

All data are synthetic. There is one product per order and no returns, taxes,
marketing or fixed overhead. Recommendations are hypotheses, not measured impact.
'''
    (root/'reports/business_case.md').write_text(report,encoding='utf-8')
    columns=['customer_id','month','region','category','product','discount_band','revenue','profit']
    template=(root/'dashboard/template.html').read_text()
    output=template.replace('__PLOTLY__',get_plotlyjs()).replace('__DATA__',clean[columns].to_json(orient='records'))
    (root/'dashboard/dashboard.html').write_text(output,encoding='utf-8')
    validation=json.loads((root/'reports/validation.json').read_text())
    validation['checks']+=['Product-discount SQL/Pandas reconciliation','90-day eligibility and repeat counts SQL/Pandas reconciliation']
    (root/'reports/validation.json').write_text(json.dumps(validation,indent=2))
