/*
SQL Problem 003: Find the Latest Order for Each Customer

Objective:
Return the most recent order placed by every customer.

Requirements:
1. A customer may have multiple orders.
2. Rank orders by order_date from newest to oldest.
3. If two orders have the same order_date, use the greater order_id
   as the latest order.
4. Include customers who have at least one order.
5. Return exactly one latest order for each customer.

Concepts:
- INNER JOIN
- Common Table Expression
- ROW_NUMBER()
- PARTITION BY
- Multiple ORDER BY conditions
*/


DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;


CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL
);


CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    order_amount NUMERIC(12, 2) NOT NULL,
    order_status VARCHAR(30) NOT NULL,

    CONSTRAINT fk_order_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


INSERT INTO customers (
    customer_id,
    customer_name,
    city
)
VALUES
    (101, 'Nilesh Thorat', 'Nashik'),
    (102, 'Priya Sharma', 'Mumbai'),
    (103, 'Rahul Patil', 'Pune'),
    (104, 'Sneha Joshi', 'Nagpur');


INSERT INTO orders (
    order_id,
    customer_id,
    order_date,
    order_amount,
    order_status
)
VALUES
    (1001, 101, '2026-06-01', 1500.00, 'COMPLETED'),
    (1002, 101, '2026-06-15', 2200.00, 'SHIPPED'),
    (1003, 101, '2026-06-15', 1800.00, 'COMPLETED'),

    (1004, 102, '2026-06-05', 900.00, 'COMPLETED'),
    (1005, 102, '2026-06-20', 1300.00, 'PENDING'),

    (1006, 103, '2026-06-10', 2500.00, 'SHIPPED');


WITH ranked_orders AS (
    SELECT
        o.order_id,
        o.customer_id,
        c.customer_name,
        c.city,
        o.order_date,
        o.order_amount,
        o.order_status,

        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY
                o.order_date DESC,
                o.order_id DESC
        ) AS order_rank

    FROM orders AS o
    INNER JOIN customers AS c
        ON o.customer_id = c.customer_id
)

SELECT
    customer_id,
    customer_name,
    city,
    order_id,
    order_date,
    order_amount,
    order_status
FROM ranked_orders
WHERE order_rank = 1
ORDER BY customer_id;