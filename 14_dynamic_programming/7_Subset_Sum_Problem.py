"""
Problem: Subset Sum Problem
Category: Dynamic Programming
Pattern: 0-1 Knapsack Boolean DP

Time Complexity:  O(N * Sum) - Filling boolean DP array
Space Complexity: O(Sum) - 1D boolean DP array
"""


# User function Template for Python3


class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return 0
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in arr:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        return 1 if dp[target] else 0


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    s = 9
    print(f"Subset with sum {s} exists: {Solution().isSubsetSum(len(arr), arr, s)}")
