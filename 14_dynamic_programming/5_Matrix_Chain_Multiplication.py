"""
Problem: Matrix Chain Multiplication
Category: Dynamic Programming
Pattern: Interval DP / Optimal Parenthesization

Time Complexity:  O(N^3) - Evaluating split points for all interval lengths
Space Complexity: O(N^2) - 2D DP matrix storage
"""


class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for length in range(2, N):
            for i in range(1, N - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
        return dp[1][N - 1]


if __name__ == "__main__":
    arr = [40, 20, 30, 10, 30]
    print(f"Min operations for matrix chain: {Solution().matrixMultiplication(len(arr), arr)}")
