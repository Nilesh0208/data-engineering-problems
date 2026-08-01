"""
Problem 014: Filter Records for Incremental Processing

Given a list of source records and a watermark timestamp, return only
records updated after the watermark.

Requirements:
1. Convert updated_at values from ISO strings to datetime objects.
2. Include only records where updated_at is greater than the watermark.
3. Do not include records updated exactly at the watermark.
4. Sort selected records by updated_at in ascending order.
5. Preserve the original record structure.
6. Return an empty list when no records qualify.
7. Raise a clear error when a timestamp is invalid.
"""

from datetime import datetime


source_records = [
    {
        "record_id": "R101",
        "customer_id": "C101",
        "amount": 1200.0,
        "updated_at": "2026-07-31T09:00:00",
    },
    {
        "record_id": "R102",
        "customer_id": "C102",
        "amount": 850.0,
        "updated_at": "2026-07-31T10:30:00",
    },
    {
        "record_id": "R103",
        "customer_id": "C103",
        "amount": 1500.0,
        "updated_at": "2026-07-31T11:15:00",
    },
    {
        "record_id": "R104",
        "customer_id": "C104",
        "amount": 700.0,
        "updated_at": "2026-07-31T10:00:00",
    },
    {
        "record_id": "R105",
        "customer_id": "C105",
        "amount": 2100.0,
        "updated_at": "2026-07-31T12:00:00",
    },
]


def filter_incremental_records(
    records: list[dict],
    watermark: str,
) -> list[dict]:
    try:
        watermark_time = datetime.fromisoformat(watermark)
    except ValueError as error:
        raise ValueError(
            f"Invalid watermark timestamp: {watermark}"
        ) from error

    incremental_records = []

    for record in records:
        updated_at_raw = record.get("updated_at")

        if updated_at_raw is None:
            raise ValueError(
                f"updated_at is missing for record: {record}"
            )

        try:
            updated_at = datetime.fromisoformat(updated_at_raw)
        except ValueError as error:
            raise ValueError(
                f"Invalid updated_at timestamp: {updated_at_raw}"
            ) from error

        if updated_at > watermark_time:
            incremental_records.append(record)

    incremental_records.sort(
        key=lambda record: datetime.fromisoformat(
            record["updated_at"]
        )
    )

    return incremental_records


result = filter_incremental_records(
    records=source_records,
    watermark="2026-07-31T10:00:00",
)

print("INCREMENTAL RECORDS")

for record in result:
    print(record)