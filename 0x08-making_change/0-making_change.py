#!/usr/bin/python3
"""
Contains a function to determine the fewest number of
coins needed to meet a given amount.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
    - coins (list of int): The values of the coins in your possession.
    - total (int): The total amount to meet.

    Returns:
    - int: The fewest number of coins needed to meet the total,
    or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
