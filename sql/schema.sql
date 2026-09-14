PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
CREATE TABLE products (
 product TEXT PRIMARY KEY, category TEXT NOT NULL,
 unit_price REAL NOT NULL, unit_cost REAL NOT NULL
);
CREATE TABLE orders (
 order_id TEXT PRIMARY KEY, order_date TEXT NOT NULL,
 customer_id TEXT NOT NULL, region TEXT NOT NULL,
 product TEXT NOT NULL REFERENCES products(product),
 category TEXT NOT NULL, unit_price REAL NOT NULL, unit_cost REAL NOT NULL,
 quantity INTEGER NOT NULL CHECK(quantity>0),
 discount REAL NOT NULL CHECK(discount BETWEEN 0 AND 1),
 shipping_cost REAL NOT NULL,
 gross_sales REAL NOT NULL, revenue REAL NOT NULL, cost REAL NOT NULL,
 profit REAL NOT NULL, month TEXT NOT NULL, discount_band TEXT NOT NULL
);
