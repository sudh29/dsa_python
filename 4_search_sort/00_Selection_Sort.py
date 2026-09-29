"""
Problem: Selection Sort
Category: Sorting Algorithms
Pattern: Comparison-Based Sorting (Unstable)

Time Complexity:  O(n^2) - Always performs n*(n-1)/2 comparisons regardless of input order
Space Complexity: O(1) - In-place sorting with constant auxiliary space
"""


def selection_sort(arr: list[int]) -> list[int]:
    """Sorts array in-place using the selection sort algorithm.

    Finds the minimum element in the unsorted portion and swaps it
    into the correct position in each pass.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
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
        actual = selection_sort(inp[:])
        assert actual == expected, f"Failed for {inp}: got {actual}, expected {expected}"
    print("All selection sort demonstrations passed!")
