"""
Problem: Heap Sort
Category: Heaps
Pattern: In-Place Max-Heap / Sift Down

Time Complexity:  O(N log N) - O(N) build heap + N log N extractions
Space Complexity: O(1) auxiliary space
"""


# User function Template for python3


class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        idx = (n - 1) // 2
        for i in range(idx, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    Solution().HeapSort(arr, len(arr))
    print(f"Sorted array: {arr}")
