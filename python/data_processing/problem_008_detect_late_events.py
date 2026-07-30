"""
Problem 008: Detect Late-Arriving Events

Given a list of event records, identify events that arrived later than
the allowed delay.

Requirements:
1. Each record contains event_time and ingested_at timestamps.
2. Calculate the delay between ingested_at and event_time.
3. An event is considered late when the delay is greater than
   the allowed delay in minutes.
4. Return late events with the calculated delay.
5. Timestamps use ISO format: YYYY-MM-DDTHH:MM:SS.
"""

from datetime import datetime


events = [
    {
        "event_id": "E101",
        "event_time": "2026-07-30T10:00:00",
        "ingested_at": "2026-07-30T10:02:00",
    },
    {
        "event_id": "E102",
        "event_time": "2026-07-30T10:05:00",
        "ingested_at": "2026-07-30T10:20:00",
    },
    {
        "event_id": "E103",
        "event_time": "2026-07-30T10:10:00",
        "ingested_at": "2026-07-30T10:14:00",
    },
    {
        "event_id": "E104",
        "event_time": "2026-07-30T10:15:00",
        "ingested_at": "2026-07-30T10:40:00",
    },
]


def detect_late_events(
    records: list[dict],
    allowed_delay_minutes: int,
) -> list[dict]:
    late_events = []

    for record in records:
        event_time = datetime.fromisoformat(record["event_time"])
        ingested_at = datetime.fromisoformat(record["ingested_at"])

        delay = ingested_at - event_time
        delay_minutes = delay.total_seconds() / 60

        if delay_minutes > allowed_delay_minutes:
            late_event = {
                **record,
                "delay_minutes": delay_minutes,
            }

            late_events.append(late_event)

    return late_events


result = detect_late_events(
    records=events,
    allowed_delay_minutes=10,
)

for event in result:
    print(event)