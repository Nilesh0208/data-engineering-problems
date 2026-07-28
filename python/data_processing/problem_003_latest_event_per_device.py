"""
Problem 003: Find the Latest Event per Device

Given a list of device events, return the latest event for each device
based on event_time.

Requirements:
1. Each device may have multiple events.
2. Keep only the event with the latest event_time.
3. Return the result as a dictionary.
4. Use device_id as the dictionary key.

Expected output:
{
    "D101": {
        "device_id": "D101",
        "status": "OFFLINE",
        "event_time": "2026-07-27T10:15:00"
    },
    "D102": {
        "device_id": "D102",
        "status": "ACTIVE",
        "event_time": "2026-07-27T10:20:00"
    }
}
"""


events = [
    {
        "device_id": "D101",
        "status": "ACTIVE",
        "event_time": "2026-07-27T10:00:00",
    },
    {
        "device_id": "D102",
        "status": "INACTIVE",
        "event_time": "2026-07-27T09:30:00",
    },
    {
        "device_id": "D101",
        "status": "OFFLINE",
        "event_time": "2026-07-27T10:15:00",
    },
    {
        "device_id": "D102",
        "status": "ACTIVE",
        "event_time": "2026-07-27T10:20:00",
    },
]


def find_latest_events(records: list[dict]) -> dict:
    latest_events = {}

    for record in records:
        device_id = record["device_id"]
        event_time = record["event_time"]

        if device_id not in latest_events:
            latest_events[device_id] = record
        else:
            stored_event_time = latest_events[device_id]["event_time"]

            if event_time > stored_event_time:
                latest_events[device_id] = record

    return latest_events

result = find_latest_events(events)

for device_id, event in result.items():
    print(device_id, event)