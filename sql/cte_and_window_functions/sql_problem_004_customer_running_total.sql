/*
SQL Problem 004: Calculate Running Total of Customer Orders

Objective:
Calculate the cumulative order amount for every customer.

Requirements:
1. Show every customer order.
2. Calculate the running total separately for each customer.
3. Process orders chronologically.
4. If two orders have the same date, use order_id as a tie-breaker.
5. Preserve every individual order row.

Concepts:
- INNER JOIN
- SUM() window function
- PARTITION BY
- ORDER BY
- ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
*/


DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;


CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL
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
    customer_name
)
VALUES
    (101, 'Nilesh Thorat'),
    (102, 'Priya Sharma'),
    (103, 'Rahul Patil');


INSERT INTO orders (
    order_id,
    customer_id,
    order_date,
    order_amount
)
VALUES
    (1001, 101, '2026-06-01', 1000.00),
    (1002, 101, '2026-06-05', 1500.00),
    (1003, 101, '2026-06-05', 500.00),
    (1004, 101, '2026-06-10', 2000.00),

    (2001, 102, '2026-06-02', 800.00),
    (2002, 102, '2026-06-08', 1200.00),
    (2003, 102, '2026-06-12', 700.00),

    (3001, 103, '2026-06-03', 2500.00);


SELECT
    o.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    o.order_amount,

    SUM(o.order_amount) OVER (
        PARTITION BY o.customer_id
        ORDER BY
            o.order_date,
            o.order_id
        ROWS BETWEEN
            UNBOUNDED PRECEDING
            AND CURRENT ROW
    ) AS running_total

FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id

ORDER BY
    o.customer_id,
    o.order_date,
    o.order_id;