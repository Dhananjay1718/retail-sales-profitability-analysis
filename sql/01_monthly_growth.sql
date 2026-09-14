WITH monthly AS (
 SELECT month, COUNT(*) orders, SUM(revenue) revenue, SUM(profit) profit
 FROM orders GROUP BY month
), previous AS (
 SELECT *, LAG(revenue) OVER (ORDER BY month) previous_revenue FROM monthly
)
SELECT month, orders, revenue, profit,
 100.0*(revenue-previous_revenue)/NULLIF(previous_revenue,0) mom_growth_pct
FROM previous ORDER BY month;
