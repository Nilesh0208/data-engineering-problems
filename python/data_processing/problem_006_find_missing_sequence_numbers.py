"""
Problem 006: Find Missing Sequence Numbers

Given a list of integer sequence numbers, identify all missing numbers
between the minimum and maximum values.

Requirements:
1. Sequence numbers may be unordered.
2. Duplicate sequence numbers may exist.
3. Return missing values in ascending order.
4. Return an empty list when there are no missing numbers.

Example input:
[101, 103, 102, 106, 103, 108]

Expected output:
[104, 105, 107]
"""


sequence_numbers = [101, 103, 102, 106, 103, 108]


def find_missing_sequence_numbers(numbers: list[int]) -> list[int]:
    if not numbers:
        return []

    unique_numbers = set(numbers)

    minimum_number = min(unique_numbers)
    maximum_number = max(unique_numbers)

    missing_numbers = []

    for number in range(minimum_number, maximum_number + 1):
        if number not in unique_numbers:
            missing_numbers.append(number)

    return missing_numbers


result = find_missing_sequence_numbers(sequence_numbers)
print(result)