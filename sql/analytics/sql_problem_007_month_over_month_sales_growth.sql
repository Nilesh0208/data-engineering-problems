/*
SQL Problem 007: Calculate Month-over-Month Sales Growth

Objective:
Calculate total sales for each month and compare each month with the
previous month.

Requirements:
1. Aggregate order amounts by calendar month.
2. Show the previous month's sales.
3. Calculate the absolute sales change.
4. Calculate month-over-month growth percentage.
5. Return NULL growth for the first month because no previous month exists.
6. Handle a previous-month total of zero safely.

Concepts:
- DATE_TRUNC()
- GROUP BY
- CTE
- LAG()
- Window functions
- Percentage growth calculation
- NULLIF()
*/


DROP TABLE IF EXISTS sales_orders;


CREATE TABLE sales_orders (
    order_id INTEGER PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id INTEGER NOT NULL,
    order_amount NUMERIC(12, 2) NOT NULL
);


INSERT INTO sales_orders (
    order_id,
    order_date,
    customer_id,
    order_amount
)
VALUES
    (1001, '2026-01-05', 101, 1000.00),
    (1002, '2026-01-12', 102, 1500.00),
    (1003, '2026-01-20', 103, 500.00),

    (1004, '2026-02-03', 101, 1200.00),
    (1005, '2026-02-14', 104, 1800.00),
    (1006, '2026-02-25', 102, 1000.00),

    (1007, '2026-03-02', 105, 900.00),
    (1008, '2026-03-11', 101, 1100.00),
    (1009, '2026-03-21', 103, 1000.00),

    (1010, '2026-04-04', 102, 2000.00),
    (1011, '2026-04-17', 104, 2500.00),
    (1012, '2026-04-28', 105, 1500.00),

    (1013, '2026-05-08', 101, 1600.00),
    (1014, '2026-05-19', 103, 1400.00);


WITH monthly_sales AS (
    SELECT
        DATE_TRUNC(
            'month',
            order_date
        )::DATE AS sales_month,

        SUM(order_amount) AS total_sales

    FROM sales_orders

    GROUP BY
        DATE_TRUNC(
            'month',
            order_date
        )
),

sales_with_previous_month AS (
    SELECT
        sales_month,
        total_sales,

        LAG(total_sales) OVER (
            ORDER BY sales_month
        ) AS previous_month_sales

    FROM monthly_sales
)

SELECT
    sales_month,
    total_sales,
    previous_month_sales,

    total_sales
    - previous_month_sales
        AS sales_change,

    ROUND(
        (
            total_sales
            - previous_month_sales
        )
        / NULLIF(previous_month_sales, 0)
        * 100,
        2
    ) AS growth_percentage

FROM sales_with_previous_month

ORDER BY sales_month;