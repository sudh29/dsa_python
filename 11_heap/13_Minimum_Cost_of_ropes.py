"""
Problem: Minimum Cost of Connecting Ropes
Category: Heaps
Pattern: Greedy / Min-Heap Huffman Variant

Time Complexity:  O(N log N) - N insertions and deletions from min-heap
Space Complexity: O(N) - Min-heap storage
"""

import heapq


class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr, n):
        heapq.heapify(arr)
        # min_heap = []
        # for i in arr:
        #     heapq.heappush(min_heap,i)
        res = 0
        while len(arr) > 1:
            val1 = heapq.heappop(arr)
            val2 = heapq.heappop(arr)
            sum_val = val1 + val2
            res += sum_val
            heapq.heappush(arr, sum_val)
        return res


if __name__ == "__main__":
    ob = Solution()
    ropes = [4, 3, 2, 6]
    print(f"Min cost to connect ropes {ropes}: {ob.minCost(ropes, len(ropes))}")
