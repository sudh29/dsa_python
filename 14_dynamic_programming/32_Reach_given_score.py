"""
Problem: Reach a Given Score (Move combinations 3, 5, 10)
Category: Dynamic Programming
Pattern: Coin Change / Unbounded Combination DP

Time Complexity:  O(N) - Three linear passes for scores 3, 5, and 10
Space Complexity: O(N) - 1D DP array
"""


class Solution:
    def count(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        moves = [3, 5, 10]
        for move in moves:
            for i in range(move, n + 1):
                dp[i] += dp[i - move]
        return dp[n]


if __name__ == "__main__":
    n = 20
    print(f"Ways to reach score {n}: {Solution().count(n)}")
