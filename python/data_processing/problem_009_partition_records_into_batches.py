"""
Problem 009: Partition Records into Fixed-Size Batches

Given a list of records, divide them into smaller batches of a fixed size.

Requirements:
1. Preserve the original order of records.
2. Each batch should contain at most batch_size records.
3. The last batch may contain fewer records.
4. Return an empty list when the input records are empty.
5. Raise an error when batch_size is zero or negative.

Example input:
records = [101, 102, 103, 104, 105, 106, 107]
batch_size = 3

Expected output:
[
    [101, 102, 103],
    [104, 105, 106],
    [107]
]
"""


records = [
    {"event_id": "E101"},
    {"event_id": "E102"},
    {"event_id": "E103"},
    {"event_id": "E104"},
    {"event_id": "E105"},
    {"event_id": "E106"},
    {"event_id": "E107"},
]


def partition_records(
    records: list[dict],
    batch_size: int,
) -> list[list[dict]]:
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than zero")

    batches = []

    for start_index in range(0, len(records), batch_size):
        end_index = start_index + batch_size
        batch = records[start_index:end_index]
        batches.append(batch)

    return batches


result = partition_records(
    records=records,
    batch_size=3,
)

for batch_number, batch in enumerate(result, start=1):
    print(f"Batch {batch_number}: {batch}")