"""
Problem 002: Find Duplicate Events

Given a list of event records, identify duplicate events based on event_id.

Requirements:
1. Return each duplicate event_id only once.
2. Preserve the order in which duplicates are first detected.
3. Return an empty list when no duplicates exist.

Example input:
[
    {"event_id": "E101", "symbol": "AAPL"},
    {"event_id": "E102", "symbol": "MSFT"},
    {"event_id": "E101", "symbol": "AAPL"},
    {"event_id": "E103", "symbol": "GOOGL"},
    {"event_id": "E102", "symbol": "MSFT"},
    {"event_id": "E102", "symbol": "MSFT"},
]

Expected output:
["E101", "E102"]
"""


events = [
    {"event_id": "E101", "symbol": "AAPL"},
    {"event_id": "E102", "symbol": "MSFT"},
    {"event_id": "E101", "symbol": "AAPL"},
    {"event_id": "E103", "symbol": "GOOGL"},
    {"event_id": "E102", "symbol": "MSFT"},
    {"event_id": "E102", "symbol": "MSFT"},
]

def find_duplicate_events(records: list[dict]) -> list[str]:
    seen_event_ids = set()
    duplicate_event_ids = set()
    duplicates = []

    for record in records:
        event_id = record["event_id"]

        if event_id in seen_event_ids:
            if event_id not in duplicate_event_ids:
                duplicates.append(event_id)
                duplicate_event_ids.add(event_id)
        else:
            seen_event_ids.add(event_id)

    return duplicates

result = find_duplicate_events(events)
print(result)