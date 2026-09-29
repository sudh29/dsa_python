"""
Problem: Optimal Strategy for a Game
Category: Dynamic Programming
Pattern: Minimax Interval DP

Time Complexity:  O(N^2) - Filling 2D table of subarray coin choices
Space Complexity: O(N^2) - 2D DP array
"""


# Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self, n, arr):
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = arr[i]
        for i in range(n - 1):
            dp[i][i + 1] = max(arr[i], arr[i + 1])
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    arr[i]
                    + min(
                        dp[i + 2][j] if i + 2 <= j else 0,
                        dp[i + 1][j - 1] if i + 1 <= j - 1 else 0,
                    ),
                    arr[j]
                    + min(
                        dp[i + 1][j - 1] if i + 1 <= j - 1 else 0,
                        dp[i][j - 2] if i <= j - 2 else 0,
                    ),
                )
        return dp[0][n - 1]


if __name__ == "__main__":
    coins = [5, 3, 7, 10]
    print(f"Max value player 1 can win: {Solution().optimalStrategyOfGame(len(coins), coins)}")
