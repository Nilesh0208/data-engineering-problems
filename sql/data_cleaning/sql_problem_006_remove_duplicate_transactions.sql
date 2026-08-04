/*
SQL Problem 006: Remove Duplicate Transactions and Keep the Latest Record

Objective:
Identify duplicate transaction records and keep only the latest
version of each transaction.

Requirements:
1. transaction_id represents the business key.
2. A transaction may appear multiple times.
3. Keep the record with the latest updated_at timestamp.
4. If timestamps are equal, keep the record with the highest record_id.
5. Display both deduplicated records and removed duplicate records.

Concepts:
- ROW_NUMBER()
- PARTITION BY
- CTE
- Deduplication
- Business key versus primary key
- Deterministic tie-breaking
*/


DROP TABLE IF EXISTS transactions;


CREATE TABLE transactions (
    record_id INTEGER PRIMARY KEY,
    transaction_id VARCHAR(20) NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    transaction_status VARCHAR(30) NOT NULL,
    updated_at TIMESTAMP NOT NULL
);


INSERT INTO transactions (
    record_id,
    transaction_id,
    customer_id,
    amount,
    transaction_status,
    updated_at
)
VALUES
    (
        1,
        'T101',
        'C101',
        1500.00,
        'PENDING',
        '2026-07-01 10:00:00'
    ),
    (
        2,
        'T102',
        'C102',
        800.00,
        'COMPLETED',
        '2026-07-01 10:05:00'
    ),
    (
        3,
        'T101',
        'C101',
        1500.00,
        'COMPLETED',
        '2026-07-01 10:10:00'
    ),
    (
        4,
        'T103',
        'C103',
        2200.00,
        'PENDING',
        '2026-07-01 10:15:00'
    ),
    (
        5,
        'T102',
        'C102',
        800.00,
        'COMPLETED',
        '2026-07-01 10:05:00'
    ),
    (
        6,
        'T104',
        'C104',
        950.00,
        'FAILED',
        '2026-07-01 10:20:00'
    ),
    (
        7,
        'T103',
        'C103',
        2200.00,
        'COMPLETED',
        '2026-07-01 10:30:00'
    );


WITH ranked_transactions AS (
    SELECT
        record_id,
        transaction_id,
        customer_id,
        amount,
        transaction_status,
        updated_at,

        ROW_NUMBER() OVER (
            PARTITION BY transaction_id
            ORDER BY
                updated_at DESC,
                record_id DESC
        ) AS duplicate_rank

    FROM transactions
)

SELECT
    record_id,
    transaction_id,
    customer_id,
    amount,
    transaction_status,
    updated_at
FROM ranked_transactions
WHERE duplicate_rank = 1
ORDER BY transaction_id;


/*
Optional query:
Display records that would be removed as duplicates.
*/

WITH ranked_transactions AS (
    SELECT
        record_id,
        transaction_id,
        customer_id,
        amount,
        transaction_status,
        updated_at,

        ROW_NUMBER() OVER (
            PARTITION BY transaction_id
            ORDER BY
                updated_at DESC,
                record_id DESC
        ) AS duplicate_rank

    FROM transactions
)

SELECT
    record_id,
    transaction_id,
    customer_id,
    amount,
    transaction_status,
    updated_at,
    duplicate_rank
FROM ranked_transactions
WHERE duplicate_rank > 1
ORDER BY
    transaction_id,
    duplicate_rank;