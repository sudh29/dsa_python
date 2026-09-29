"""
Problem: Merge Sort
Category: Sorting Algorithms
Pattern: Divide and Conquer (Stable)

Time Complexity:  O(n log n) - Always divides in half and merges linearly
Space Complexity: O(n) - Requires auxiliary arrays for merging at each level
"""


def merge_sort(arr: list[int]) -> list[int]:
    """Sorts array in-place using the merge sort algorithm.

    Recursively divides the array into halves, sorts each half,
    then merges the sorted halves back together.
    """
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


if __name__ == "__main__":
    test_cases = [
        ([5, 2, 6, 7, 2, 1, 0, 3], [0, 1, 2, 2, 3, 5, 6, 7]),
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([-3, -1, -2, 0], [-3, -2, -1, 0]),
    ]
    for inp, expected in test_cases:
        actual = merge_sort(inp[:])
        assert actual == expected, f"Failed for {inp}: got {actual}, expected {expected}"
    print("All merge sort demonstrations passed!")
