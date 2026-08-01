/*
SQL Problem 002: Find Customers Who Have Never Placed an Order

Objective:
Return customers who exist in the customers table but do not have
any matching rows in the orders table.

Concepts:
- LEFT JOIN
- NULL filtering
- Anti-join pattern
- NOT EXISTS alternative
*/

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;


CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    signup_date DATE NOT NULL
);


CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    order_amount NUMERIC(12, 2) NOT NULL,
    CONSTRAINT fk_order_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


INSERT INTO customers (
    customer_id,
    customer_name,
    city,
    signup_date
)
VALUES
    (101, 'Nilesh Thorat', 'Nashik', '2026-01-10'),
    (102, 'Priya Sharma', 'Mumbai', '2026-02-15'),
    (103, 'Rahul Patil', 'Pune', '2026-03-05'),
    (104, 'Sneha Joshi', 'Nagpur', '2026-04-12'),
    (105, 'Amit Verma', 'Thane', '2026-05-01');


INSERT INTO orders (
    order_id,
    customer_id,
    order_date,
    order_amount
)
VALUES
    (1001, 101, '2026-06-01', 1500.00),
    (1002, 102, '2026-06-02', 2200.00),
    (1003, 101, '2026-06-05', 800.00),
    (1004, 104, '2026-06-07', 1200.00);


SELECT
    c.customer_id,
    c.customer_name,
    c.city,
    c.signup_date
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
ORDER BY c.customer_id;