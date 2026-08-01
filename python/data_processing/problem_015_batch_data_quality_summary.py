"""
Problem 015: Generate Data Quality Summary by Batch

Given a list of processed records, calculate a batch-level data quality
summary.

Requirements:
1. Count total records.
2. Count valid records.
3. Count rejected records.
4. Calculate rejection rate as a percentage.
5. Assign health status:
   - HEALTHY: rejection rate < 5%
   - WARNING: rejection rate >= 5% and < 20%
   - CRITICAL: rejection rate >= 20%
6. Return zero values safely when the input list is empty.
"""


processed_records = [
    {
        "record_id": "R101",
        "status": "VALID",
    },
    {
        "record_id": "R102",
        "status": "VALID",
    },
    {
        "record_id": "R103",
        "status": "REJECTED",
    },
    {
        "record_id": "R104",
        "status": "VALID",
    },
    {
        "record_id": "R105",
        "status": "REJECTED",
    },
    {
        "record_id": "R106",
        "status": "VALID",
    },
    {
        "record_id": "R107",
        "status": "VALID",
    },
    {
        "record_id": "R108",
        "status": "VALID",
    },
    {
        "record_id": "R109",
        "status": "VALID",
    },
    {
        "record_id": "R110",
        "status": "VALID",
    },
]


def build_data_quality_summary(
    records: list[dict],
) -> dict[str, int | float | str]:
    total_records = len(records)

    valid_records = 0
    rejected_records = 0

    for record in records:
        status = record.get("status")

        if status == "VALID":
            valid_records += 1
        elif status == "REJECTED":
            rejected_records += 1

    if total_records == 0:
        rejection_rate = 0.0
    else:
        rejection_rate = (
            rejected_records / total_records
        ) * 100

    if rejection_rate >= 20:
        health_status = "CRITICAL"
    elif rejection_rate >= 5:
        health_status = "WARNING"
    else:
        health_status = "HEALTHY"

    return {
        "total_records": total_records,
        "valid_records": valid_records,
        "rejected_records": rejected_records,
        "rejection_rate_pct": round(rejection_rate, 2),
        "health_status": health_status,
    }


result = build_data_quality_summary(processed_records)

for key, value in result.items():
    print(f"{key}: {value}")