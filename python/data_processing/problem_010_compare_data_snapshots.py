"""
Problem 010: Compare Two Data Snapshots

Given an old snapshot and a new snapshot of customer records,
identify inserted, updated, deleted, and unchanged records.

Requirements:
1. Match records using customer_id.
2. A record is inserted when it exists only in the new snapshot.
3. A record is deleted when it exists only in the old snapshot.
4. A record is updated when the customer exists in both snapshots,
   but one or more business fields have changed.
5. A record is unchanged when both versions are identical.
6. Return all four categories separately.
"""


old_snapshot = [
    {
        "customer_id": "C101",
        "name": "Nilesh Thorat",
        "city": "Pune",
        "active": True,
    },
    {
        "customer_id": "C102",
        "name": "Priya Sharma",
        "city": "Mumbai",
        "active": True,
    },
    {
        "customer_id": "C103",
        "name": "Rahul Patil",
        "city": "Nagpur",
        "active": True,
    },
]


new_snapshot = [
    {
        "customer_id": "C101",
        "name": "Nilesh Thorat",
        "city": "Nashik",
        "active": True,
    },
    {
        "customer_id": "C102",
        "name": "Priya Sharma",
        "city": "Mumbai",
        "active": True,
    },
    {
        "customer_id": "C104",
        "name": "Sneha Joshi",
        "city": "Pune",
        "active": True,
    },
]


def compare_snapshots(
    old_records: list[dict],
    new_records: list[dict],
) -> dict[str, list]:
    old_by_id = {
        record["customer_id"]: record
        for record in old_records
    }

    new_by_id = {
        record["customer_id"]: record
        for record in new_records
    }

    inserted = []
    updated = []
    deleted = []
    unchanged = []

    for customer_id, new_record in new_by_id.items():
        if customer_id not in old_by_id:
            inserted.append(new_record)
            continue

        old_record = old_by_id[customer_id]

        if new_record == old_record:
            unchanged.append(new_record)
        else:
            updated.append(
                {
                    "customer_id": customer_id,
                    "old_record": old_record,
                    "new_record": new_record,
                }
            )

    for customer_id, old_record in old_by_id.items():
        if customer_id not in new_by_id:
            deleted.append(old_record)

    return {
        "inserted": inserted,
        "updated": updated,
        "deleted": deleted,
        "unchanged": unchanged,
    }


result = compare_snapshots(
    old_records=old_snapshot,
    new_records=new_snapshot,
)

for category, records in result.items():
    print(f"\n{category.upper()}")

    for record in records:
        print(record)