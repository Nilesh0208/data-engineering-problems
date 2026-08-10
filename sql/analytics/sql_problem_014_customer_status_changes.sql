/*
SQL Problem 014:
Compare Current and Previous Customer Status

Objective:
Detect status changes for each customer.

Requirements:
1. A customer may have multiple status records.
2. Compare each status with the previous status.
3. Identify actual status transitions.
4. Ignore the first record for each customer.
5. Ignore rows where status did not change.
6. Return the previous status and current status.

Concepts:
- LAG()
- PARTITION BY
- Window functions
- Change detection
- CDC-style logic
*/


DROP TABLE IF EXISTS customer_status_history;


CREATE TABLE customer_status_history (
    record_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    status VARCHAR(30) NOT NULL,
    status_time TIMESTAMP NOT NULL
);


INSERT INTO customer_status_history (
    record_id,
    customer_id,
    status,
    status_time
)
VALUES
    (1, 101, 'NEW',
        '2026-07-01 09:00:00'),

    (2, 101, 'ACTIVE',
        '2026-07-03 10:00:00'),

    (3, 101, 'ACTIVE',
        '2026-07-05 11:00:00'),

    (4, 101, 'SUSPENDED',
        '2026-07-10 12:00:00'),

    (5, 101, 'ACTIVE',
        '2026-07-15 09:30:00'),

    (6, 102, 'NEW',
        '2026-07-02 08:00:00'),

    (7, 102, 'ACTIVE',
        '2026-07-04 09:00:00'),

    (8, 102, 'CLOSED',
        '2026-07-20 10:00:00'),

    (9, 103, 'ACTIVE',
        '2026-07-01 07:00:00'),

    (10, 103, 'ACTIVE',
        '2026-07-08 08:00:00');


WITH status_comparison AS (
    SELECT
        record_id,
        customer_id,
        status_time,
        status AS current_status,

        LAG(status) OVER (
            PARTITION BY customer_id
            ORDER BY
                status_time,
                record_id
        ) AS previous_status

    FROM customer_status_history
)

SELECT
    record_id,
    customer_id,
    status_time,
    previous_status,
    current_status,

    previous_status
    || ' -> '
    || current_status
        AS status_transition

FROM status_comparison

WHERE previous_status IS NOT NULL
  AND current_status <> previous_status

ORDER BY
    customer_id,
    status_time,
    record_id;