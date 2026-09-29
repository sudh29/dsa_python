"""
Problem: Smallest Range Covering Elements from K Lists
Category: Heaps
Pattern: Min-Heap / K Pointers

Time Complexity:  O(N * K * log K) where N is max list length
Space Complexity: O(K) - Heap storing one element per list
"""

import heapq


class Solution:
    def smallestRange(self, KSortedArray, n, k):
        low = 0
        high = 0
        range_val = float("inf")
        max_val = float("-inf")
        min_val = float("inf")
        heap = []
        i = 0
        for j in range(k):
            heapq.heappush(heap, (KSortedArray[j][i], i, j, len(KSortedArray[j])))
            min_val = min(min_val, KSortedArray[j][i])
            max_val = max(max_val, KSortedArray[j][i])

        while len(heap) > 0:
            min_element, a, b, arr_len = heapq.heappop(heap)
            if range_val > max_val - min_element:
                min_val = min_element
                range_val = max_val - min_val
                low = min_val
                high = max_val
            if a + 1 < arr_len:
                a += 1
                heapq.heappush(heap, (KSortedArray[b][a], a, b, arr_len))
                max_val = max(max_val, KSortedArray[b][a])
            else:
                break
        return [low, high]


if __name__ == "__main__":
    lists = [[1, 3, 5, 7, 9], [0, 2, 4, 8, 10], [2, 3, 5, 7, 11]]
    res = Solution().smallestRange(lists, 5, 3)
    print(f"Smallest range: {res}")
