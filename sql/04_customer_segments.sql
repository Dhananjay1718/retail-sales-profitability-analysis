WITH customers AS (
 SELECT customer_id, COUNT(*) orders, SUM(revenue) revenue, SUM(profit) profit
 FROM orders GROUP BY customer_id
), segments AS (
 SELECT *, CASE WHEN orders>=2 THEN 'Repeat' ELSE 'One-time' END segment
 FROM customers
)
SELECT segment, COUNT(*) customers, SUM(orders) orders,
 SUM(revenue) revenue, SUM(profit) profit
FROM segments GROUP BY segment ORDER BY segment;
