"""
Problem: Kth Smallest Number Again
Category: Searching & Sorting
Pattern: Interval Merging / Binary Search

Time Complexity:  O(N log N + Q * M) where N is number of intervals, M is merged intervals, Q is queries
Space Complexity: O(N) - Storage for merged intervals
"""


def kth_smallest_number_again(intervals: list[tuple[int, int]], queries: list[int]) -> list[int]:
    """Finds the k-th smallest number after merging overlapping intervals.

    Args:
        intervals: List of (start, end) inclusive integer intervals.
        queries: List of 1-indexed k values to find.

    Returns:
        List of answers for each query (-1 if k exceeds total numbers).
    """
    if not intervals:
        return [-1] * len(queries)

    sorted_intervals = sorted(intervals)
    merged = [list(sorted_intervals[0])]

    for curr_start, curr_end in sorted_intervals[1:]:
        if merged[-1][1] >= curr_start:
            merged[-1][1] = max(merged[-1][1], curr_end)
        else:
            merged.append([curr_start, curr_end])

    results = []
    for k in queries:
        ans = -1
        rem = k
        for start, end in merged:
            count = end - start + 1
            if count >= rem:
                ans = start + rem - 1
                break
            rem -= count
        results.append(ans)

    return results


if __name__ == "__main__":
    test_intervals = [(1, 5), (10, 15)]
    test_queries = [3, 6, 12]
    expected = [3, 10, -1]
    actual = kth_smallest_number_again(test_intervals, test_queries)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print(f"Kth smallest number again demo passed: {actual}")
