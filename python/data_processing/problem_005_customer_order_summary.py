"""
Problem 005: Group Orders by Customer and Calculate Summary

Given a list of order records, generate a summary for each customer.

Requirements:
1. Ignore orders with status "CANCELLED".
2. Calculate total order amount for each customer.
3. Count the number of valid orders for each customer.
4. Calculate average order amount.
5. Return the result as a dictionary using customer_id as the key.

Expected output:
{
    "C101": {
        "total_amount": 2200.0,
        "order_count": 2,
        "average_amount": 1100.0
    },
    "C102": {
        "total_amount": 1500.0,
        "order_count": 2,
        "average_amount": 750.0
    }
}
"""


orders = [
    {
        "order_id": "O101",
        "customer_id": "C101",
        "amount": 1200,
        "status": "COMPLETED",
    },
    {
        "order_id": "O102",
        "customer_id": "C102",
        "amount": 800,
        "status": "COMPLETED",
    },
    {
        "order_id": "O103",
        "customer_id": "C101",
        "amount": 1000,
        "status": "SHIPPED",
    },
    {
        "order_id": "O104",
        "customer_id": "C103",
        "amount": 500,
        "status": "CANCELLED",
    },
    {
        "order_id": "O105",
        "customer_id": "C102",
        "amount": 700,
        "status": "SHIPPED",
    },
]


def build_customer_order_summary(
    records: list[dict],
) -> dict[str, dict]:
    customer_summary = {}

    for record in records:
        customer_id = record["customer_id"]
        amount = float(record["amount"])
        status = record["status"]

        if status == "CANCELLED":
            continue

        if customer_id not in customer_summary:
            customer_summary[customer_id] = {
                "total_amount": 0.0,
                "order_count": 0,
            }

        customer_summary[customer_id]["total_amount"] += amount
        customer_summary[customer_id]["order_count"] += 1

    for customer_id, summary in customer_summary.items():
        total_amount = summary["total_amount"]
        order_count = summary["order_count"]

        summary["average_amount"] = total_amount / order_count

    return customer_summary


result = build_customer_order_summary(orders)

for customer_id, summary in result.items():
    print(customer_id, summary)