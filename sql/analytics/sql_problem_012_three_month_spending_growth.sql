/*
SQL Problem 012:
Find Customers Whose Spending Increased
for 3 Consecutive Months

Objective:
Identify customers whose monthly spending
increased for three consecutive months.

Requirements:
1. Aggregate sales by customer and month.
2. Compare each month with the previous month.
3. Identify months where spending increased.
4. Find customers with at least 3 consecutive
   monthly increases.
5. Return streak start, end, and streak length.

Concepts:
- DATE_TRUNC()
- SUM()
- LAG()
- CTE
- Window functions
- Gaps and islands
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
    (1002, 101, '2026-02-10', 1500.00),
    (1003, 101, '2026-03-15', 2000.00),
    (1004, 101, '2026-04-20', 2500.00),
    (1005, 101, '2026-05-12', 1800.00),

    (2001, 102, '2026-01-08', 2000.00),
    (2002, 102, '2026-02-11', 1800.00),
    (2003, 102, '2026-03-18', 2200.00),
    (2004, 102, '2026-04-22', 2100.00),

    (3001, 103, '2026-01-04', 500.00),
    (3002, 103, '2026-02-05', 700.00),
    (3003, 103, '2026-03-06', 900.00),
    (3004, 103, '2026-04-07', 1200.00),
    (3005, 103, '2026-05-08', 1500.00);


WITH monthly_spending AS (
    SELECT
        customer_id,
        DATE_TRUNC(
            'month',
            order_date
        )::DATE AS spend_month,
        SUM(order_amount) AS total_spending
    FROM customer_orders
    GROUP BY
        customer_id,
        DATE_TRUNC(
            'month',
            order_date
        )
),

spending_with_previous AS (
    SELECT
        customer_id,
        spend_month,
        total_spending,

        LAG(total_spending) OVER (
            PARTITION BY customer_id
            ORDER BY spend_month
        ) AS previous_month_spending

    FROM monthly_spending
),

growth_months AS (
    SELECT
        customer_id,
        spend_month,
        total_spending,

        CASE
            WHEN total_spending
                 > previous_month_spending
            THEN 1
            ELSE 0
        END AS increased_flag

    FROM spending_with_previous
),

numbered_growth AS (
    SELECT
        customer_id,
        spend_month,
        total_spending,

        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY spend_month
        ) AS rn_all,

        ROW_NUMBER() OVER (
            PARTITION BY
                customer_id,
                increased_flag
            ORDER BY spend_month
        ) AS rn_flag,

        increased_flag

    FROM growth_months
),

grouped_growth AS (
    SELECT
        customer_id,
        spend_month,
        total_spending,
        increased_flag,

        rn_all - rn_flag AS growth_group

    FROM numbered_growth
),

growth_streaks AS (
    SELECT
        customer_id,
        MIN(spend_month) AS streak_start_month,
        MAX(spend_month) AS streak_end_month,
        COUNT(*) AS consecutive_increase_months
    FROM grouped_growth
    WHERE increased_flag = 1
    GROUP BY
        customer_id,
        growth_group
)

SELECT
    customer_id,
    streak_start_month,
    streak_end_month,
    consecutive_increase_months

FROM growth_streaks

WHERE consecutive_increase_months >= 3

ORDER BY
    customer_id,
    streak_start_month;