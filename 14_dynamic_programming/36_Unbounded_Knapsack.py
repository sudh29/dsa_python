"""
Problem: Unbounded Knapsack
Category: Dynamic Programming
Pattern: 1D DP / Repeated Item Usage

Time Complexity:  O(N * W) - Iterating through weights for each item
Space Complexity: O(W) - 1D DP array storage
"""


class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0] * (W + 1)
        for i in range(N):
            for j in range(wt[i], W + 1):
                dp[j] = max(dp[j], dp[j - wt[i]] + val[i])
        return dp[W]


if __name__ == "__main__":
    val = [1, 1]
    wt = [2, 1]
    w = 3
    print(f"Unbounded knapsack max value: {Solution().knapSack(len(val), w, val, wt)}")
