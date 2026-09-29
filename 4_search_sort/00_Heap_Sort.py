"""
Problem: Heap Sort
Category: Sorting Algorithms
Pattern: Selection-Based Sorting using Binary Heap (Unstable, In-Place)

Time Complexity:  O(n log n) - Build heap O(n), then n extract-max operations each O(log n)
Space Complexity: O(1) - In-place sorting using implicit max-heap in the array
"""


def heapify(arr: list[int], n: int, i: int) -> None:
    """Maintains the max-heap property for the subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: list[int]) -> list[int]:
    """Sorts array in-place using the heap sort algorithm.

    Builds a max-heap from the array, then repeatedly extracts the maximum
    element and places it at the end of the array.
    """
    n = len(arr)
    # Build max-heap (bottom-up)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    test_cases = [
        ([12, 11, 13, 5, 6, 7], [5, 6, 7, 11, 12, 13]),
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([-3, -1, -2, 0], [-3, -2, -1, 0]),
    ]
    for inp, expected in test_cases:
        actual = heap_sort(inp[:])
        assert actual == expected, f"Failed for {inp}: got {actual}, expected {expected}"
    print("All heap sort demonstrations passed!")
