SELECT region, COUNT(*) orders, SUM(revenue) revenue, SUM(profit) profit,
 SUM(revenue)/COUNT(*) aov,
 100.0*SUM(profit)/NULLIF(SUM(revenue),0) margin_pct,
 DENSE_RANK() OVER (ORDER BY SUM(profit) DESC) profit_rank
FROM orders GROUP BY region ORDER BY profit_rank;
