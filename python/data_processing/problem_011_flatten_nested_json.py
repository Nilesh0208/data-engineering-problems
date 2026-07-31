"""
Problem 011: Flatten Nested JSON Records

Given a list of nested event records, convert each record into a flat
dictionary suitable for loading into a database table.

Requirements:
1. Flatten nested dictionaries using an underscore between keys.
2. Preserve non-dictionary values such as strings, numbers, lists,
   Booleans, and None.
3. Support multiple levels of nested dictionaries.
4. Preserve the original order of records.
5. Return an empty list when the input list is empty.

Example:
{
    "event_id": "E101",
    "customer": {
        "customer_id": "C101",
        "location": {
            "city": "Nashik",
            "state": "Maharashtra"
        }
    }
}

Becomes:
{
    "event_id": "E101",
    "customer_customer_id": "C101",
    "customer_location_city": "Nashik",
    "customer_location_state": "Maharashtra"
}
"""


events = [
    {
        "event_id": "E101",
        "event_type": "order_created",
        "customer": {
            "customer_id": "C101",
            "name": "Nilesh Thorat",
            "location": {
                "city": "Nashik",
                "state": "Maharashtra",
            },
        },
        "order": {
            "order_id": "O501",
            "amount": 1500.0,
            "items": ["Laptop Stand", "Keyboard"],
        },
        "active": True,
    },
    {
        "event_id": "E102",
        "event_type": "order_created",
        "customer": {
            "customer_id": "C102",
            "name": "Priya Sharma",
            "location": {
                "city": "Mumbai",
                "state": "Maharashtra",
            },
        },
        "order": {
            "order_id": "O502",
            "amount": 2200.0,
            "items": ["Monitor"],
        },
        "active": True,
    },
]


def flatten_dictionary(
    record: dict,
    parent_key: str = "",
    separator: str = "_",
) -> dict:
    flattened_record = {}

    for key, value in record.items():
        if parent_key:
            flattened_key = f"{parent_key}{separator}{key}"
        else:
            flattened_key = key

        if isinstance(value, dict):
            nested_values = flatten_dictionary(
                record=value,
                parent_key=flattened_key,
                separator=separator,
            )

            flattened_record.update(nested_values)
        else:
            flattened_record[flattened_key] = value

    return flattened_record


def flatten_records(records: list[dict]) -> list[dict]:
    flattened_records = []

    for record in records:
        flattened_record = flatten_dictionary(record)
        flattened_records.append(flattened_record)

    return flattened_records


result = flatten_records(events)

for event in result:
    print(event)