"""
Problem: Chocolate Distribution Problem
Category: Greedy Algorithms
Pattern: Sorting / Sliding Window of Size M

Time Complexity:  O(N log N) - Sorting packets by chocolate count
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def findMinDiff(self, A, N, M):
        A.sort()
        res = float("inf")
        for i in range(0, N - M + 1):
            res = min(res, A[i + M - 1] - A[i])
        return res


if __name__ == "__main__":
    packets = [3, 4, 1, 9, 56, 7, 9, 12]
    m = 5
    print(f"Min difference for {m} students: {Solution().findMinDiff(packets, len(packets), m)}")
