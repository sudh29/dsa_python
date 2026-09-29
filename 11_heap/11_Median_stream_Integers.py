"""
Problem: Find Median in a Data Stream
Category: Heaps
Pattern: Two Heaps (Max-Heap & Min-Heap)

Time Complexity:  O(log N) per insertion, O(1) per median query
Space Complexity: O(N) - Storage for two balanced heaps
"""

import heapq
import math


class Solution:
    def __init__(self):
        self.a = []  # Max heap
        self.b = []  # Min heap
        self.median = 0

    def balanceHeaps(self):
        temp = -heapq.heappop(self.a)
        heapq.heappush(self.b, temp)
        if len(self.b) > len(self.a):
            temp = heapq.heappop(self.b)
            heapq.heappush(self.a, -temp)

    def getMedian(self):
        if len(self.a) != len(self.b):
            self.median = -self.a[0]
        else:
            self.median = (-self.a[0] + self.b[0]) / 2
        return self.median

    def insertHeaps(self, x):
        heapq.heappush(self.a, -x)
        self.balanceHeaps()


if __name__ == "__main__":
    import math

    ob = Solution()
    for x in [5, 15, 1, 3]:
        ob.insertHeaps(x)
        print(f"Inserted {x}, median = {math.floor(ob.getMedian())}")
