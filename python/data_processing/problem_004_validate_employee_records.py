"""
Problem 004: Validate and Normalize Employee Records

Given a list of raw employee records:

1. Convert employee_id to an integer.
2. Remove extra spaces from employee names.
3. Convert employee names to title case.
4. Convert experience to a float.
5. Convert active values to Boolean.
6. Reject records with:
   - Missing employee_id
   - Missing or empty name
   - Negative experience
   - Invalid data types

Return:
- A list of valid cleaned records
- A list of rejected records with rejection reasons
"""


raw_records = [
    {
        "employee_id": "101",
        "name": "  nilesh thorat ",
        "experience": "3.5",
        "active": 1,
    },
    {
        "employee_id": "102",
        "name": "PRIYA SHARMA",
        "experience": "5",
        "active": 0,
    },
    {
        "employee_id": "",
        "name": "Rahul Patil",
        "experience": "2",
        "active": 1,
    },
    {
        "employee_id": "104",
        "name": "   ",
        "experience": "4",
        "active": 1,
    },
    {
        "employee_id": "105",
        "name": "Amit Kumar",
        "experience": "-1",
        "active": 1,
    },
    {
        "employee_id": "ABC",
        "name": "Sneha Joshi",
        "experience": "3",
        "active": 1,
    },
]


def validate_and_clean_employees(
    records: list[dict],
) -> tuple[list[dict], list[dict]]:
    valid_records = []
    rejected_records = []

    for record in records:
        try:
            employee_id_raw = record.get("employee_id")
            name_raw = record.get("name")
            experience_raw = record.get("experience")
            active_raw = record.get("active")

            if employee_id_raw in (None, ""):
                raise ValueError("employee_id is missing")

            if name_raw is None or not str(name_raw).strip():
                raise ValueError("name is missing or empty")

            employee_id = int(employee_id_raw)
            name = str(name_raw).strip().title()
            experience = float(experience_raw)
            active = bool(active_raw)

            if experience < 0:
                raise ValueError("experience cannot be negative")

            cleaned_record = {
                "employee_id": employee_id,
                "name": name,
                "experience": experience,
                "active": active,
            }

            valid_records.append(cleaned_record)

        except (ValueError, TypeError) as error:
            rejected_record = {
                "original_record": record,
                "rejection_reason": str(error),
            }

            rejected_records.append(rejected_record)

    return valid_records, rejected_records


valid_employees, rejected_employees = validate_and_clean_employees(
    raw_records
)

print("Valid records:")

for employee in valid_employees:
    print(employee)

print("\nRejected records:")

for employee in rejected_employees:
    print(employee)