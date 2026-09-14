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
