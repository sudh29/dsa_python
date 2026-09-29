"""
Problem: Merge K Sorted Arrays
Category: Heaps
Pattern: Min-Heap / K-Way Merge

Time Complexity:  O(N * K * log K) where N is array length
Space Complexity: O(K) heap space + O(N * K) output array
"""

import heapq


class Solution:
    # Function to merge k sorted arrays.
    def mergeKArrays(self, arr, k):
        min_heap = []
        for i in range(k):
            for j in range(k):
                heapq.heappush(min_heap, arr[i][j])

        res = [heapq.heappop(min_heap) for _ in range(k * k)]
        # print(res)
        return res


if __name__ == "__main__":
    ob = Solution()
    arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Merged arrays: {ob.mergeKArrays(arrays, len(arrays))}")
