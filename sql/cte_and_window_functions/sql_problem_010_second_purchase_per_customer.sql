/*
SQL Problem 010:
Find the Second Purchase Date for Each Customer

Objective:
Return the second purchase made by each customer.

Requirements:
1. A customer may have multiple orders.
2. Rank orders chronologically per customer.
3. If two orders have the same date,
   use order_id as a tie-breaker.
4. Return only the second order.
5. Exclude customers with fewer than two orders.

Concepts:
- ROW_NUMBER()
- PARTITION BY
- ORDER BY
- CTE
- Customer transaction sequencing
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
    (101, 'Amit Sharma'),
    (102, 'Priya Patil'),
    (103, 'Rahul Joshi'),
    (104, 'Neha Verma');


INSERT INTO orders (
    order_id,
    customer_id,
    order_date,
    order_amount
)
VALUES
    (1001, 101, '2026-01-05', 1000.00),
    (1002, 101, '2026-01-15', 1500.00),
    (1003, 101, '2026-02-01', 1800.00),

    (2001, 102, '2026-01-10', 900.00),
    (2002, 102, '2026-01-10', 1100.00),
    (2003, 102, '2026-01-25', 1300.00),

    (3001, 103, '2026-02-05', 2500.00),

    (4001, 104, '2026-03-01', 700.00),
    (4002, 104, '2026-03-12', 1200.00);


WITH ranked_orders AS (
    SELECT
        o.order_id,
        o.customer_id,
        c.customer_name,
        o.order_date,
        o.order_amount,

        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY
                o.order_date,
                o.order_id
        ) AS purchase_number

    FROM orders AS o

    INNER JOIN customers AS c
        ON o.customer_id = c.customer_id
)

SELECT
    customer_id,
    customer_name,
    order_id,
    order_date AS second_purchase_date,
    order_amount
FROM ranked_orders
WHERE purchase_number = 2
ORDER BY customer_id;