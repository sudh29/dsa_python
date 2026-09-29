"""
Problem: Partition Equal Subset Sum
Category: Dynamic Programming
Pattern: Subset Sum / 0-1 Knapsack

Time Complexity:  O(N * sum) - Pseudo-polynomial DP table filling
Space Complexity: O(sum) - 1D boolean DP array
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
    arr = [1, 5, 11, 5]
    print(f"Equal partition possible: {Solution().equalPartition(len(arr), arr)}")
