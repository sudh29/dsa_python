"""
Problem: Check if Array is Sorted (Recursive)
Category: Search & Sort
Pattern: Recursion (Divide and Conquer)

Time Complexity:  O(n) - Checks each adjacent pair once
Space Complexity: O(n) - Recursion stack depth (could be O(1) iteratively)
"""


def is_sorted_recursive(arr: list[int]) -> bool:
    """Checks whether the array is sorted in non-decreasing order using recursion.

    Args:
        arr: The list of integers to check.

    Returns:
        True if the array is sorted in non-decreasing order, False otherwise.
    """
    if len(arr) <= 1:
        return True
    return arr[0] <= arr[1] and is_sorted_recursive(arr[1:])


def is_sorted_iterative(arr: list[int]) -> bool:
    """Checks whether the array is sorted in non-decreasing order (iterative, O(1) space)."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], True),
        ([1, 5, 671, 1, 6, 3, 2, 0], False),
        ([], True),
        ([1], True),
        ([1, 1, 1, 1], True),
        ([5, 4], False),
    ]
    for arr, expected in test_cases:
        assert is_sorted_recursive(arr) == expected, f"Recursive failed for {arr}"
        assert is_sorted_iterative(arr) == expected, f"Iterative failed for {arr}"
    print("All sorted check demonstrations passed!")
