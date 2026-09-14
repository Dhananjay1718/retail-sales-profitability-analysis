# Executive summary

Synthetic educational dataset; computed results, not actual company performance.

| KPI | Value |
|---|---:|
| Orders | 6,000 |
| Observed customers | 2,269 |
| Revenue | INR 120,568,915.00 |
| Illustrative profit | INR 18,536,370.00 |
| Weighted margin | 15.37% |
| Average order value | INR 20,094.82 |
| Repeat customer rate | 75.54% |

## Five answers

1. **Sales trend:** peak revenue is 2025-04 at INR 11,764,732.50.
   See 01_monthly_growth.csv for monthly growth. First-month growth is undefined.
   Review staffing around peaks; one year cannot prove recurring seasonality.
2. **Products:** Notebook has the lowest total profit at
   INR 61,682.50. 0 products have negative total profit.
   Inspect loss orders and unit economics before changing prices or assortment.
   Lowest profit is not the same as negative profit.
3. **Discounts:** High (>10%) has the lowest weighted margin,
   -0.72%. Test discount limits within product categories.
   Revenue mechanically falls with discount at fixed quantity; this comparison
   does not estimate demand response or causal campaign benefit.
4. **Customers:** 1,714 of
   2,269 observed customers ordered at least twice (75.54%).
   Propose a randomized second-purchase campaign; this is not cohort retention.
5. **Regions:** North ranks first on total profit
   (INR 5,707,092.50). Compare margin and AOV alongside volume before
   reallocating resources. Unknown regions remain in the totals.

## Scope and limitations

Calendar year 2025; INR; one single-product order per row.
Profit subtracts product and shipping costs only. No returns, tax, marketing or
fixed overhead. Synthetic patterns cannot justify real market decisions.
Recommendations are untested hypotheses. No percentage improvement is claimed.
