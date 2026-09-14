-- Require full follow-up; later-date orders within 90 days qualify.
WITH first_orders AS (
 SELECT customer_id,MIN(order_date) first_date FROM orders GROUP BY customer_id
), followup AS (
 SELECT f.customer_id,f.first_date,
 MAX(CASE WHEN o.order_date>f.first_date
 AND o.order_date<=DATE(f.first_date,'+90 days') THEN 1 ELSE 0 END) repeated
 FROM first_orders f JOIN orders o ON f.customer_id=o.customer_id
 WHERE DATE(f.first_date,'+90 days')<='2025-12-31'
 GROUP BY f.customer_id,f.first_date
)
SELECT SUBSTR(first_date,1,7) first_purchase_month,COUNT(*) eligible_customers,
 SUM(repeated) repeat_customers,100.0*SUM(repeated)/COUNT(*) repeat_90d_pct
FROM followup GROUP BY SUBSTR(first_date,1,7) ORDER BY first_purchase_month;
