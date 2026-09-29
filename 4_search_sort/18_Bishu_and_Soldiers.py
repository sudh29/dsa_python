"""
Problem: Bishu and Soldiers
Category: Searching & Sorting
Pattern: Binary Search / Prefix Sums

Time Complexity:  O(N log N + Q log N) - Sorting soldiers takes O(N log N), each query takes O(log N)
Space Complexity: O(N) - Storing prefix sums for cumulative soldier power
"""

import bisect


def bishu_and_soldiers(soldier_powers: list[int], queries: list[int]) -> list[tuple[int, int]]:
    """Calculates number of defeated soldiers and cumulative power for each query.

    Args:
        soldier_powers: List of soldier power ratings.
        queries: List of Bishu's power for each round.

    Returns:
        List of tuples (count_defeated, total_strength).
    """
    sorted_powers = sorted(soldier_powers)
    prefix_sum = [0]
    for p in sorted_powers:
        prefix_sum.append(prefix_sum[-1] + p)

    results = []
    for q in queries:
        idx = bisect.bisect_right(sorted_powers, q)
        results.append((idx, prefix_sum[idx]))
    return results


if __name__ == "__main__":
    soldiers = [1, 2, 3, 4, 5, 6, 7]
    queries = [3, 10, 2]
    expected = [(3, 6), (7, 28), (2, 3)]
    actual = bishu_and_soldiers(soldiers, queries)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print(f"Bishu and Soldiers demo passed: {actual}")
