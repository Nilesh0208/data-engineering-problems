/*
SQL Problem 015:
Detect Missing Daily Sales Dates

Objective:
Identify calendar dates where no sales records exist
between the minimum and maximum order date.

Requirements:
1. Find the minimum and maximum sales dates.
2. Generate every calendar date in that range.
3. Compare and generated dates with actual sales dates.
4. Return only missing dates.
5. Avoid duplicate dates caused by multiple orders
   on the same sales day.

Concepts:
- GENERATE_SERIES()
- MIN()
- MAX()
- CTE
- LEFT JOIN
- Anti-join pattern
- Date completeness checks
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
    (1001, '2026-07-01', 101, 1000.00),
    (1002, '2026-07-01', 102, 500.00),

    (1003, '2026-07-02', 103, 1200.00),

    (1004, '2026-07-04', 101, 800.00),

    (1005, '2026-07-05', 104, 1600.00),

    (1006, '2026-07-08', 102, 900.00),

    (1007, '2026-07-08', 105, 1100.00),

    (1008, '2026-07-10', 103, 1400.00);


WITH date_boundaries AS (
    SELECT
        MIN(order_date) AS min_date,
        MAX(order_date) AS max_date
    FROM sales_orders
),

calendar_dates AS (
    SELECT
        GENERATE_SERIES(
            min_date,
            max_date,
            INTERVAL '1 day'
        )::DATE AS calendar_date
    FROM date_boundaries
),

actual_sales_dates AS (
    SELECT DISTINCT
        order_date
    FROM sales_orders
)

SELECT
    c.calendar_date AS missing_sales_date
FROM calendar_dates AS c

LEFT JOIN actual_sales_dates AS a
    ON c.calendar_date = a.order_date

WHERE a.order_date IS NULL

ORDER BY c.calendar_date;
