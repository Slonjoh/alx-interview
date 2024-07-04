#!/usr/bin/python3
"""
Module: 0-prime_game

Contains a function to determine the winner of the prime number game.
"""


def sieve(n):
    """ Use the Sieve of Eratosthenes to find all primes <= n """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(n + 1) if is_prime[p]]


def count_primes_up_to(n, primes):
    """ Count the number of primes <= n """
    count = 0
    for prime in primes:
        if prime > n:
            break
        count += 1
    return count


def isWinner(x, nums):
    """
    Determines the winner of the prime number game.

    Args:
    - x (int): The number of rounds.
    - nums (list of int): The list of n values for each round.

    Returns:
    - str: The name of the player that won the most rounds.
    - If the winner cannot be determined, return None.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n, primes)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
