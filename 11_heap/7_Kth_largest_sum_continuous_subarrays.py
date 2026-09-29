"""
Problem: K-th Largest Sum Contiguous Subarray
Category: Heaps
Pattern: Prefix Sums / Min-Heap of Size K

Time Complexity:  O(N^2 log K) - Evaluates all subarrays maintaining min-heap of size K
Space Complexity: O(K) - Min-heap storage
"""

from typing import List
import heapq


class Solution:
    def kthLargest(self, N: int, K: int, arr: List[int]) -> int:
        sum_val = [0] * (N + 1)
        for i in range(1, N + 1):
            sum_val[i] = sum_val[i - 1] + arr[i - 1]
        # print(sum_val)
        min_heap = []
        heapq.heapify(min_heap)
        for i in range(1, N + 1):
            for j in range(i, N + 1):
                x = sum_val[j] - sum_val[i - 1]
                if len(min_heap) < K:
                    heapq.heappush(min_heap, x)
                else:
                    if min_heap[0] < x:
                        heapq.heappop(min_heap)
                        heapq.heappush(min_heap, x)
        # print(min_heap)
        return min_heap[0]


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        return []

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    obj = Solution()
    arr = [2, 6, 4, 1]
    k = 3
    print(f"{k}-th largest contiguous sum: {obj.kthLargest(len(arr), k, arr)}")
