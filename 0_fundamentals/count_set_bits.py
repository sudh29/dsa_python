"""
Problem: Count Set Bits (Counting 1s in Binary Representation)
Category: Fundamentals / Bit Manipulation
Pattern: Dynamic Programming on Bits

Time Complexity:  O(n) - Uses DP recurrence; O(n log n) with naive approach
Space Complexity: O(n) - Result array for 0..n
"""


def count_bits_dp(n: int) -> list[int]:
    """Counts the number of 1-bits for every integer from 0 to n using DP.

    Uses the recurrence: count(i) = count(i // 2) + (i % 2)
    """
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    return result


def count_bits_naive(n: int) -> list[int]:
    """Counts set bits for 0..n by converting each number to binary."""
    return [bin(i).count("1") for i in range(n + 1)]


if __name__ == "__main__":
    test_cases = [
        (0, [0]),
        (1, [0, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
    ]
    for n, expected in test_cases:
        assert count_bits_dp(n) == expected, f"DP failed for {n}"
        assert count_bits_naive(n) == expected, f"Naive failed for {n}"
    print("All count bits demonstrations passed!")
