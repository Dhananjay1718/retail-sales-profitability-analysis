SELECT p.category, o.product, COUNT(*) orders,
 SUM(o.revenue) revenue, SUM(o.profit) profit,
 100.0*SUM(o.profit)/NULLIF(SUM(o.revenue),0) margin_pct,
 SUM(CASE WHEN o.profit<0 THEN 1 ELSE 0 END) loss_orders
FROM orders o JOIN products p ON o.product=p.product
GROUP BY p.category, o.product ORDER BY profit;
