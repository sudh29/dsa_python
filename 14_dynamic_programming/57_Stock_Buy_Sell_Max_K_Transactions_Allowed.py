"""
Problem: Stock Buy and Sell Max K Transactions Allowed
Category: Dynamic Programming
Pattern: 2D DP with Max Diff Optimization

Time Complexity:  O(K * N) - Filling K x N transaction matrix
Space Complexity: O(K * N) - DP table storage
"""


class Solution:
    def maxProfit(self, K, N, A):
        if N == 0:
            return 0
        dp = [[0] * N for _ in range(K + 1)]
        for t in range(1, K + 1):
            max_so_far = -A[0]
            for d in range(1, N):
                dp[t][d] = max(dp[t][d - 1], A[d] + max_so_far)
                max_so_far = max(max_so_far, dp[t - 1][d] - A[d])
        return dp[K][N - 1]


if __name__ == "__main__":
    prices = [10, 22, 5, 75, 65, 80]
    k = 2
    print(f"Max profit for {k} transactions: {Solution().maxProfit(k, len(prices), prices)}")
