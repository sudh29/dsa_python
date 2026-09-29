"""
Problem: 0-1 Knapsack Problem
Category: Dynamic Programming
Pattern: 0-1 Knapsack / 2D to 1D Space Optimization

Time Complexity:  O(N * W) - Iterating items and remaining capacity
Space Complexity: O(W) - Space-optimized 1D DP array
"""


class Solution:
    def knapSack(self, W, wt, val, n):
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1])
                else:
                    dp[i][w] = dp[i - 1][w]
        return dp[n][W]


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    w = 50
    print(f"0-1 Knapsack max value: {Solution().knapSack(w, wt, val, len(val))}")
