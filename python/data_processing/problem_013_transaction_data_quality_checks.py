"""
Problem 013: Identify Data Quality Issues in Transactions

Given a list of transaction records, validate each record and classify it
as valid or rejected.

Validation rules:
1. transaction_id must be present and non-empty.
2. customer_id must be present and non-empty.
3. amount must be numeric and greater than zero.
4. currency must be one of: INR, USD, EUR.
5. status must be one of: COMPLETED, PENDING, FAILED.
6. Return valid records separately from rejected records.
7. Each rejected record must include all rejection reasons.
"""


transactions = [
    {
        "transaction_id": "T101",
        "customer_id": "C101",
        "amount": 1500,
        "currency": "INR",
        "status": "COMPLETED",
    },
    {
        "transaction_id": "",
        "customer_id": "C102",
        "amount": 800,
        "currency": "USD",
        "status": "COMPLETED",
    },
    {
        "transaction_id": "T103",
        "customer_id": "",
        "amount": -500,
        "currency": "INR",
        "status": "FAILED",
    },
    {
        "transaction_id": "T104",
        "customer_id": "C104",
        "amount": "1200",
        "currency": "GBP",
        "status": "COMPLETED",
    },
    {
        "transaction_id": "T105",
        "customer_id": "C105",
        "amount": "invalid",
        "currency": "EUR",
        "status": "UNKNOWN",
    },
]


ALLOWED_CURRENCIES = {"INR", "USD", "EUR"}
ALLOWED_STATUSES = {"COMPLETED", "PENDING", "FAILED"}


def validate_transactions(
    records: list[dict],
) -> tuple[list[dict], list[dict]]:
    valid_records = []
    rejected_records = []

    for record in records:
        rejection_reasons = []

        transaction_id = record.get("transaction_id")
        customer_id = record.get("customer_id")
        amount_raw = record.get("amount")
        currency = record.get("currency")
        status = record.get("status")

        if transaction_id is None or not str(transaction_id).strip():
            rejection_reasons.append(
                "transaction_id is missing or empty"
            )

        if customer_id is None or not str(customer_id).strip():
            rejection_reasons.append(
                "customer_id is missing or empty"
            )

        try:
            amount = float(amount_raw)

            if amount <= 0:
                rejection_reasons.append(
                    "amount must be greater than zero"
                )

        except (TypeError, ValueError):
            amount = None
            rejection_reasons.append(
                "amount must be numeric"
            )

        if currency not in ALLOWED_CURRENCIES:
            rejection_reasons.append(
                f"unsupported currency: {currency}"
            )

        if status not in ALLOWED_STATUSES:
            rejection_reasons.append(
                f"unsupported status: {status}"
            )

        if rejection_reasons:
            rejected_records.append(
                {
                    "original_record": record,
                    "rejection_reasons": rejection_reasons,
                }
            )
        else:
            valid_records.append(
                {
                    "transaction_id": str(transaction_id).strip(),
                    "customer_id": str(customer_id).strip(),
                    "amount": amount,
                    "currency": currency,
                    "status": status,
                }
            )

    return valid_records, rejected_records


valid_transactions, rejected_transactions = validate_transactions(
    transactions
)

print("VALID TRANSACTIONS")

for transaction in valid_transactions:
    print(transaction)

print("\nREJECTED TRANSACTIONS")

for transaction in rejected_transactions:
    print(transaction)