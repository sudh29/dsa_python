"""
Problem: Convert Min Heap to Max Heap
Category: Heaps
Pattern: Bottom-Up Max-Heapify

Time Complexity:  O(N) - Linear time build-heap algorithm
Space Complexity: O(log N) - Recursion stack for heapify
"""


def max_heapify(arr, N, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < N and arr[left] > arr[largest]:
        largest = left
    if right < N and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, N, largest)


class Solution:
    def convertMinToMaxHeap(self, N, arr):
        idx = N // 2 - 1
        for i in range(idx, -1, -1):
            max_heapify(arr, N, i)


if __name__ == "__main__":
    ob = Solution()
    arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    ob.convertMinToMaxHeap(len(arr), arr)
    print(f"Converted to max heap: {arr}")
