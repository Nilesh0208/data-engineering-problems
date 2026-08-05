/*
SQL Problem 008: Calculate a 3-Day Rolling Average of Daily Sales

Objective:
Calculate daily sales and a rolling average based on the current day
and the previous two available sales days.

Requirements:
1. Aggregate order amounts by order date.
2. Return one row for each sales date.
3. Calculate a 3-row rolling sales total.
4. Calculate a 3-row rolling average.
5. Include partial windows for the first two rows.
6. Round the rolling average to two decimal places.

Concepts:
- DATE aggregation
- GROUP BY
- CTE
- SUM() window function
- AVG() window function
- ROWS BETWEEN
*/


DROP TABLE IF EXISTS daily_orders;


CREATE TABLE daily_orders (
    order_id INTEGER PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id INTEGER NOT NULL,
    order_amount NUMERIC(12, 2) NOT NULL
);


INSERT INTO daily_orders (
    order_id,
    order_date,
    customer_id,
    order_amount
)
VALUES
    (1001, '2026-07-01', 101, 1000.00),
    (1002, '2026-07-01', 102, 500.00),

    (1003, '2026-07-02', 103, 1200.00),

    (1004, '2026-07-03', 101, 800.00),
    (1005, '2026-07-03', 104, 700.00),

    (1006, '2026-07-04', 105, 2000.00),

    (1007, '2026-07-05', 102, 900.00),

    (1008, '2026-07-06', 103, 1600.00),
    (1009, '2026-07-06', 101, 400.00),

    (1010, '2026-07-07', 104, 1100.00);


WITH daily_sales AS (
    SELECT
        order_date,
        SUM(order_amount) AS total_sales
    FROM daily_orders
    GROUP BY order_date
)

SELECT
    order_date,
    total_sales,

    SUM(total_sales) OVER (
        ORDER BY order_date
        ROWS BETWEEN
            2 PRECEDING
            AND CURRENT ROW
    ) AS rolling_3_day_total,

    ROUND(
        AVG(total_sales) OVER (
            ORDER BY order_date
            ROWS BETWEEN
                2 PRECEDING
                AND CURRENT ROW
        ),
        2
    ) AS rolling_3_day_average

FROM daily_sales

ORDER BY order_date;