"""
Problem: Bubble Sort
Category: Sorting Algorithms
Pattern: Comparison-Based Sorting (Stable)

Time Complexity:  O(n^2) - Nested loops comparing adjacent elements; O(n) best case with early termination
Space Complexity: O(1) - In-place sorting with constant auxiliary space
"""


def bubble_sort(arr: list[int]) -> list[int]:
    """Sorts array in-place using the optimized bubble sort algorithm.

    Uses an early-termination flag to stop if no swaps occur in a pass,
    achieving O(n) best-case for already-sorted inputs.
    """
    n = len(arr)
    for k in range(1, n):
        swapped = False
        for i in range(n - k):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    test_cases = [
        ([8, 2, 6, 7, 2, 1, 0, 3], [0, 1, 2, 2, 3, 6, 7, 8]),
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([-3, -1, -2, 0], [-3, -2, -1, 0]),
    ]
    for inp, expected in test_cases:
        actual = bubble_sort(inp[:])
        assert actual == expected, f"Failed for {inp}: got {actual}, expected {expected}"
    print("All bubble sort demonstrations passed!")
