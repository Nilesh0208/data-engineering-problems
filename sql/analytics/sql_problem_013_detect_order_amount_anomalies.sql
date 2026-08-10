/*
SQL Problem 013:
Detect Orders With Suspicious Amount Changes

Objective:
Identify customer orders where the order amount changes
significantly compared with the customer's previous order.

Requirements:
1. Compare each order with the customer's previous order.
2. Calculate absolute amount difference.
3. Calculate percentage change.
4. Flag orders where change is greater than 50%.
5. Ignore the first order for each customer.

Concepts:
- LAG()
- PARTITION BY
- Window functions
- Percentage change
- NULLIF()
- CASE
*/


DROP TABLE IF EXISTS customer_orders;


CREATE TABLE customer_orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    order_amount NUMERIC(12, 2) NOT NULL
);


INSERT INTO customer_orders (
    order_id,
    customer_id,
    order_date,
    order_amount
)
VALUES
    (1001, 101, '2026-01-05', 1000.00),
    (1002, 101, '2026-01-10', 1100.00),
    (1003, 101, '2026-01-15', 2500.00),
    (1004, 101, '2026-01-20', 2400.00),

    (2001, 102, '2026-01-03', 800.00),
    (2002, 102, '2026-01-08', 700.00),
    (2003, 102, '2026-01-13', 300.00),

    (3001, 103, '2026-01-01', 1500.00),
    (3002, 103, '2026-01-05', 1600.00),
    (3003, 103, '2026-01-10', 1700.00);


WITH order_comparison AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        order_amount,

        LAG(order_amount) OVER (
            PARTITION BY customer_id
            ORDER BY
                order_date,
                order_id
        ) AS previous_order_amount

    FROM customer_orders
),

order_changes AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        order_amount,
        previous_order_amount,

        order_amount
        - previous_order_amount
            AS amount_difference,

        ROUND(
            (
                order_amount
                - previous_order_amount
            )
            / NULLIF(
                previous_order_amount,
                0
            )
            * 100,
            2
        ) AS percentage_change

    FROM order_comparison
)

SELECT
    order_id,
    customer_id,
    order_date,
    previous_order_amount,
    order_amount,
    amount_difference,
    percentage_change,

    CASE
        WHEN ABS(percentage_change) > 50
        THEN 'SUSPICIOUS'
        ELSE 'NORMAL'
    END AS anomaly_status

FROM order_changes

WHERE previous_order_amount IS NOT NULL

ORDER BY
    customer_id,
    order_date,
    order_id;