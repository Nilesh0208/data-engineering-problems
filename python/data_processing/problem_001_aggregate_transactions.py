"""
Problem 001: Aggregate Transactions by Customer

Given a list of transaction records, calculate the total transaction
amount for each customer.

Requirements:
1. Ignore transactions with a negative amount.
2. Combine multiple transactions belonging to the same customer.
3. Return the totals as a dictionary.

Example input:
[
    {"customer_id": "C101", "amount": 1200},
    {"customer_id": "C102", "amount": 800},
    {"customer_id": "C101", "amount": 500},
    {"customer_id": "C103", "amount": -200},
    {"customer_id": "C102", "amount": 300},
]

Expected output:
{
    "C101": 1700,
    "C102": 1100
}
"""


transactions = [
    {"customer_id": "C101", "amount": 1200},
    {"customer_id": "C102", "amount": 800},
    {"customer_id": "C101", "amount": 500},
    {"customer_id": "C103", "amount": -200},
    {"customer_id": "C102", "amount": 300},
]


def aggregate_transactions(records: list[dict]) -> dict:
    customer_totals = {}

    for record in records:
        customer_id = record["customer_id"]
        amount = record["amount"]

        if amount < 0:
            continue

        if customer_id in customer_totals:
            customer_totals[customer_id] += amount
        else:
            customer_totals[customer_id] = amount

    return customer_totals


result = aggregate_transactions(transactions)
print(result)