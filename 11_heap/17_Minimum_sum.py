"""
Problem: Minimum Sum of Two Numbers Formed from Digits of an Array
Category: Heaps
Pattern: Greedy / Sorting / Alternating Digits

Time Complexity:  O(N log N) - Sorting the digit array
Space Complexity: O(N) - Result string representation
"""

import heapq


class Solution:
    def solve(self, arr, n):
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        heapq.heapify(arr)
        num1 = 0
        num2 = 0
        while len(arr) > 1:
            num1 = num1 * 10 + heapq.heappop(arr)
            num2 = num2 * 10 + heapq.heappop(arr)
        if len(arr) == 1:
            num1 = num1 * 10 + heapq.heappop(arr)
        return num1 + num2


if __name__ == "__main__":
    ob = Solution()
    arr = [6, 8, 4, 5, 2, 3]
    print(f"Min sum for {arr}: {ob.solve(arr, len(arr))}")
