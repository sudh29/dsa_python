"""
Problem: Insertion Sort
Category: Sorting Algorithms
Pattern: Comparison-Based Sorting (Stable, Adaptive)

Time Complexity:  O(n^2) - Shifts elements in worst case; O(n) best case for nearly sorted arrays
Space Complexity: O(1) - In-place sorting with constant auxiliary space
"""


def insertion_sort(arr: list[int]) -> list[int]:
    """Sorts array in-place using the insertion sort algorithm.

    Iterates through the array, inserting each element into its correct
    position among the already-sorted prefix by shifting larger elements right.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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
        actual = insertion_sort(inp[:])
        assert actual == expected, f"Failed for {inp}: got {actual}, expected {expected}"
    print("All insertion sort demonstrations passed!")
