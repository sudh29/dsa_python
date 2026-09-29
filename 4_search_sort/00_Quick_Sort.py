"""
Problem: Quick Sort
Category: Sorting Algorithms
Pattern: Divide and Conquer (Unstable, In-Place)

Time Complexity:  O(n log n) average, O(n^2) worst case - Randomized pivot mitigates worst case
Space Complexity: O(log n) - Recursion stack depth for balanced partitions
"""

import random


def partition(arr: list[int], low: int, high: int) -> int:
    """Lomuto partition scheme with randomized pivot selection."""
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr: list[int], low: int = 0, high: int | None = None) -> list[int]:
    """Sorts array in-place using the quick sort algorithm with randomized pivot.

    Uses Lomuto partition scheme. Random pivot selection ensures O(n log n)
    expected time even for adversarial inputs.
    """
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


if __name__ == "__main__":
    test_cases = [
        ([5, 22, -6, 7, 2, 1, 0, 3], [-6, 0, 1, 2, 3, 5, 7, 22]),
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([-3, -1, -2, 0], [-3, -2, -1, 0]),
    ]
    for inp, expected in test_cases:
        actual = quick_sort(inp[:])
        assert actual == expected, f"Failed for {inp}: got {actual}, expected {expected}"
    print("All quick sort demonstrations passed!")
