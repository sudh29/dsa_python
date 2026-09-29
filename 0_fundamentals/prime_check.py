"""
Problem: Prime Number Check
Category: Fundamentals
Pattern: Trial Division (Optimized)

Time Complexity:  O(√n) - Only checks odd divisors up to square root
Space Complexity: O(1) - Constant auxiliary space
"""

import math


def is_prime(n: int) -> bool:
    """Checks whether a number is prime using optimized trial division.

    Handles edge cases (1, 2, even numbers) and only tests odd divisors
    up to √n for efficiency.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.isqrt(n)
    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    test_cases = [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (25, False),
        (97, True),
        (100, False),
        (0, False),
        (-5, False),
    ]
    for n, expected in test_cases:
        assert is_prime(n) == expected, f"Failed for {n}: expected {expected}"
    print("All prime check demonstrations passed!")
