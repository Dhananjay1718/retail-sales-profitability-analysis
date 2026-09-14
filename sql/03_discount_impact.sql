SELECT discount_band, COUNT(*) orders, SUM(revenue) revenue, SUM(profit) profit,
 100.0*AVG(discount) average_discount_pct,
 100.0*SUM(profit)/NULLIF(SUM(revenue),0) margin_pct
FROM orders GROUP BY discount_band ORDER BY margin_pct;
