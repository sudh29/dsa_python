"""
Problem: Egg Dropping Puzzle
Category: Dynamic Programming
Pattern: Minimax DP / Binary Search Optimization

Time Complexity:  O(N * K) with binary search / O(N * K^2) standard DP
Space Complexity: O(N * K) - DP table for eggs and floors
"""


class Solution:
    def eggDrop(self, N, K):
        if N == 1:
            return K
        if K == 0:
            return 0

        dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

        for i in range(1, N + 1):
            dp[i][1] = 1
            dp[i][0] = 0

        for j in range(1, K + 1):
            dp[1][j] = j

        for i in range(2, N + 1):
            for j in range(2, K + 1):
                dp[i][j] = float("inf")
                for x in range(1, j + 1):
                    res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                    dp[i][j] = min(dp[i][j], res)
        return dp[N][K]


if __name__ == "__main__":
    n, k = 2, 10
    print(f"Min drops for {n} eggs and {k} floors: {Solution().eggDrop(n, k)}")
