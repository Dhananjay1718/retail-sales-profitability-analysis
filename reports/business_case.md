# Business case: prioritize discount economics

## Decision and evidence
Investigate discount economics before recommending more sales volume.
The high-discount band has **-0.72% contribution margin**
across 1,548 orders in this synthetic case.

| Finding | Interpretation | Proposed next step |
|---|---|---|
| 463 loss-making orders | Positive product totals can hide weak transactions | Review price and shipping costs at order level |
| Negative margin in the high-discount band | Overall averages may hide product mix | Compare bands within products using SQL 07 |
| 46.03% repeat within 90 days | Comparable follow-up for 2,105 eligible customers | Design a second-purchase experiment |
| 164 customers excluded from 90-day analysis | Late entrants have insufficient follow-up | Do not count these customers as non-repeaters |

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
