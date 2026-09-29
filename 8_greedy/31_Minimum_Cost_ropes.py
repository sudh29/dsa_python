"""
Problem: Minimum Cost of Connecting Ropes
Category: Greedy Algorithms
Pattern: Min-Heap / Huffman Combine

Time Complexity:  O(N log N) - Repeatedly extracting min two ropes
Space Complexity: O(N) - Min-heap storage
"""

import heapq


class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr, n):
        # arr.sort()
        # A = arr
        # res = 0
        # while len(A)>1:
        #     a = A.pop(0)
        #     b = A.pop(0)
        #     cost = a+b
        #     res+=cost
        #     A.append(cost)
        #     A.sort()
        # return res

        heapq.heapify(arr)
        res = 0
        while len(arr) > 1:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            cost = a + b
            res += cost
            heapq.heappush(arr, cost)
        return res


if __name__ == "__main__":
    ropes = [4, 3, 2, 6]
    print(f"Min cost: {Solution().minCost(ropes, len(ropes))}")
