# SQL

Dialect: SQLite. Open retail.db in a SQLite client and run the numbered .sql files.
The Python build creates schema.sql, loads data, runs queries and exports results.

| File | Skills demonstrated |
|---|---|
| 01_monthly_growth.sql | CTE, LAG, NULLIF |
| 02_product_profitability.sql | JOIN, GROUP BY, conditional aggregation |
| 03_discount_impact.sql | Weighted ratios, aggregation |
| 04_customer_segments.sql | CTE, CASE, customer-level grouping |
| 05_regional_performance.sql | DENSE_RANK, AOV, margin |
| 06_loss_making_products.sql | HAVING after aggregation |

First-month growth is NULL because no prior month exists.
products.product is unique, preventing JOIN fanout.
COUNT(*) equals orders only because this dataset has one row per order.
For real line-item data use distinct order counts.

Practice: explain WHERE versus HAVING, why averages of margins can mislead,
how a nonunique dimension inflates sums, and how LAG differs from a self JOIN.

## Additional diagnostics
SQL 07 compares discount bands within products to reveal product-mix differences.
SQL 08 measures repeat purchase within 90 days among customers with a complete
follow-up window. Late first-time buyers are excluded, not labelled non-repeaters.
Only later-date orders qualify; same-day extra orders do not. This differs from
SQL 04's frequency metric. Neither measure is cohort retention. Both new queries
are reconciled against independent Pandas calculations.
