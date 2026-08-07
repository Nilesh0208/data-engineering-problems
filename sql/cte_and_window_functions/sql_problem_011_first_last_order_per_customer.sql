/*
SQL Problem 011:
Find First and Last Order for Each Customer

Objective:
Return each customer's first and latest order details.

Requirements:
1. A customer may have multiple orders.
2. Identify first order chronologically.
3. Identify latest order chronologically.
4. Use order_id as tie-breaker.
5. Return one row per customer.

Concepts:
- ROW_NUMBER()
- PARTITION BY
- CTE
- Conditional aggregation
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
    (1002, 101, '2026-01-20', 1500.00),
    (1003, 101, '2026-02-10', 2000.00),

    (2001, 102, '2026-01-15', 800.00),
    (2002, 102, '2026-03-05', 1200.00),

    (3001, 103, '2026-02-01', 2500.00),

    (4001, 104, '2026-01-10', 500.00),
    (4002, 104, '2026-01-10', 700.00),
    (4003, 104, '2026-04-01', 1800.00);


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
        ) AS first_rank,

        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY
                o.order_date DESC,
                o.order_id DESC
        ) AS last_rank

    FROM orders AS o

    INNER JOIN customers AS c
        ON o.customer_id = c.customer_id
)

SELECT
    customer_id,
    customer_name,

    MAX(
        CASE
            WHEN first_rank = 1
            THEN order_id
        END
    ) AS first_order_id,

    MAX(
        CASE
            WHEN first_rank = 1
            THEN order_date
        END
    ) AS first_order_date,

    MAX(
        CASE
            WHEN first_rank = 1
            THEN order_amount
        END
    ) AS first_order_amount,

    MAX(
        CASE
            WHEN last_rank = 1
            THEN order_id
        END
    ) AS last_order_id,

    MAX(
        CASE
            WHEN last_rank = 1
            THEN order_date
        END
    ) AS last_order_date,

    MAX(
        CASE
            WHEN last_rank = 1
            THEN order_amount
        END
    ) AS last_order_amount

FROM ranked_orders

GROUP BY
    customer_id,
    customer_name

ORDER BY customer_id;