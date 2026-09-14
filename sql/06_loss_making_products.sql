SELECT product, SUM(profit) total_profit FROM orders
GROUP BY product HAVING SUM(profit)<0 ORDER BY total_profit;
