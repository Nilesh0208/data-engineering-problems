"""
Problem 007: Merge Customer Records by Latest Update

Given a list of customer records, keep only the latest record for each
customer based on updated_at.

Requirements:
1. A customer may appear multiple times.
2. Keep the record with the latest updated_at timestamp.
3. Ignore inactive customer records in the final result.
4. Return the result as a dictionary keyed by customer_id.
5. Input timestamps use ISO format: YYYY-MM-DDTHH:MM:SS.
"""


customer_records = [
    {
        "customer_id": "C101",
        "name": "Nilesh Thorat",
        "city": "Pune",
        "active": True,
        "updated_at": "2026-07-20T10:00:00",
    },
    {
        "customer_id": "C102",
        "name": "Priya Sharma",
        "city": "Mumbai",
        "active": True,
        "updated_at": "2026-07-20T11:00:00",
    },
    {
        "customer_id": "C101",
        "name": "Nilesh Thorat",
        "city": "Nashik",
        "active": True,
        "updated_at": "2026-07-21T09:30:00",
    },
    {
        "customer_id": "C103",
        "name": "Rahul Patil",
        "city": "Nagpur",
        "active": False,
        "updated_at": "2026-07-21T12:00:00",
    },
    {
        "customer_id": "C102",
        "name": "Priya Sharma",
        "city": "Thane",
        "active": False,
        "updated_at": "2026-07-22T08:45:00",
    },
    {
        "customer_id": "C104",
        "name": "Sneha Joshi",
        "city": "Pune",
        "active": True,
        "updated_at": "2026-07-22T10:15:00",
    },
]


def merge_latest_customer_records(
    records: list[dict],
) -> dict[str, dict]:
    latest_records = {}

    for record in records:
        customer_id = record["customer_id"]
        updated_at = record["updated_at"]

        if customer_id not in latest_records:
            latest_records[customer_id] = record
        else:
            stored_updated_at = latest_records[customer_id]["updated_at"]

            if updated_at > stored_updated_at:
                latest_records[customer_id] = record

    active_customers = {}

    for customer_id, record in latest_records.items():
        if record["active"]:
            active_customers[customer_id] = record

    return active_customers


result = merge_latest_customer_records(customer_records)

for customer_id, record in result.items():
    print(customer_id, record)