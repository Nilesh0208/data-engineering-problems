/*
SQL Problem 005: Find Consecutive Login Days

Objective:
Identify continuous login streaks for each user.

Requirements:
1. A user may log in multiple times on the same day.
2. Count each calendar date only once.
3. Group consecutive dates into streaks.
4. Return the start date, end date, and streak length.
5. Return only streaks of at least 3 consecutive days.

Concepts:
- DISTINCT
- ROW_NUMBER()
- Date arithmetic
- CTEs
- Gaps and islands pattern
- GROUP BY
*/


DROP TABLE IF EXISTS user_logins;


CREATE TABLE user_logins (
    login_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    login_time TIMESTAMP NOT NULL
);


INSERT INTO user_logins (
    login_id,
    user_id,
    login_time
)
VALUES
    (1, 101, '2026-07-01 09:00:00'),
    (2, 101, '2026-07-01 18:00:00'),
    (3, 101, '2026-07-02 10:00:00'),
    (4, 101, '2026-07-03 11:00:00'),
    (5, 101, '2026-07-05 09:30:00'),
    (6, 101, '2026-07-06 09:45:00'),
    (7, 101, '2026-07-07 10:00:00'),
    (8, 101, '2026-07-08 10:15:00'),

    (9, 102, '2026-07-01 08:00:00'),
    (10, 102, '2026-07-03 08:30:00'),
    (11, 102, '2026-07-04 09:00:00'),
    (12, 102, '2026-07-05 09:15:00'),

    (13, 103, '2026-07-10 12:00:00'),
    (14, 103, '2026-07-11 12:30:00');


WITH distinct_login_dates AS (
    SELECT DISTINCT
        user_id,
        login_time::DATE AS login_date
    FROM user_logins
),

numbered_logins AS (
    SELECT
        user_id,
        login_date,

        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY login_date
        ) AS row_number
    FROM distinct_login_dates
),

grouped_logins AS (
    SELECT
        user_id,
        login_date,

        login_date
        - (row_number::INTEGER * INTERVAL '1 day')
            AS streak_group
    FROM numbered_logins
),

login_streaks AS (
    SELECT
        user_id,
        MIN(login_date) AS streak_start_date,
        MAX(login_date) AS streak_end_date,
        COUNT(*) AS consecutive_days
    FROM grouped_logins
    GROUP BY
        user_id,
        streak_group
)

SELECT
    user_id,
    streak_start_date,
    streak_end_date,
    consecutive_days
FROM login_streaks
WHERE consecutive_days >= 3
ORDER BY
    user_id,
    streak_start_date;