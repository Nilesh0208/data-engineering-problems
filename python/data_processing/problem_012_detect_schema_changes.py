"""
Problem 012: Detect Schema Changes Between Two Records

Compare an old record schema with a new record schema and identify:

1. Added fields
2. Removed fields
3. Fields whose data types changed
4. Unchanged fields

The schema is inferred from dictionary keys and Python value types.
"""


old_record = {
    "customer_id": "C101",
    "name": "Nilesh Thorat",
    "age": 25,
    "active": True,
    "credit_limit": 50000.0,
}

new_record = {
    "customer_id": "C101",
    "name": "Nilesh Thorat",
    "age": "25",
    "active": True,
    "city": "Nashik",
}


def detect_schema_changes(
    old_schema_record: dict,
    new_schema_record: dict,
) -> dict[str, list]:
    old_fields = set(old_schema_record)
    new_fields = set(new_schema_record)

    added_fields = sorted(new_fields - old_fields)
    removed_fields = sorted(old_fields - new_fields)

    common_fields = old_fields & new_fields

    type_changed_fields = []
    unchanged_fields = []

    for field in sorted(common_fields):
        old_type = type(old_schema_record[field]).__name__
        new_type = type(new_schema_record[field]).__name__

        if old_type != new_type:
            type_changed_fields.append(
                {
                    "field": field,
                    "old_type": old_type,
                    "new_type": new_type,
                }
            )
        else:
            unchanged_fields.append(field)

    return {
        "added_fields": added_fields,
        "removed_fields": removed_fields,
        "type_changed_fields": type_changed_fields,
        "unchanged_fields": unchanged_fields,
    }


result = detect_schema_changes(
    old_schema_record=old_record,
    new_schema_record=new_record,
)

for category, values in result.items():
    print(f"\n{category.upper()}")

    for value in values:
        print(value)