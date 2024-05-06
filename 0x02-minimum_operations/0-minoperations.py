#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve
    exactly n H characters.
    """
    if n <= 1:
        return 0

    # The number of operations
    operations = 0
    # Starting with a single 'H', count current characters
    current_chars = 1

    # Factorize n to determine optimal copy and paste strategy
    for factor in range(2, n + 1):
        while n % factor == 0:
            operations += factor
            n //= factor

    return operations
