-- Diagnose product mix before interpreting aggregate discount margins.
SELECT product, discount_band, COUNT(*) AS orders,
 SUM(revenue) AS revenue, SUM(profit) AS profit,
 100.0*SUM(profit)/NULLIF(SUM(revenue),0) AS margin_pct
FROM orders GROUP BY product,discount_band ORDER BY product,discount_band;
