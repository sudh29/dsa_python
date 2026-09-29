"""
Problem: Merge Two Binary Max Heaps
Category: Heaps
Pattern: Concatenate & Build-Heap

Time Complexity:  O(N + M) - Linear time build heap on concatenated arrays
Space Complexity: O(N + M) - Merged array storage
"""


def heapify(arr, n, i):
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


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


class Solution:
    def mergeHeaps(self, a, b, n, m):
        # max_heap = []
        # i,j=0,0
        # while i<n and j<m:
        #     if a[i]>b[j]:
        #         heapq.heappush(max_heap,a[i])
        #         i+=1
        #     else:
        #         heapq.heappush(max_heap,b[j])
        #         j+=1
        # while i<n:
        #     heapq.heappush(max_heap,a[i])
        #     i+=1
        # while j<m:
        #     heapq.heappush(max_heap,b[j])
        #     j+=1
        # heapq._heapify_max(max_heap)
        # return max_heap

        merged_heap = a + b
        build_max_heap(merged_heap)
        return merged_heap


if __name__ == "__main__":
    obj = Solution()
    h1, h2 = [10, 5, 6, 2], [12, 7, 9]
    res = obj.mergeHeaps(h1, h2, len(h1), len(h2))
    print(f"Merged heap: {res}")
