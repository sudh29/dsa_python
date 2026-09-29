"""
Problem: Maximum Path Sum in Matrix
Category: Dynamic Programming
Pattern: 2D Grid DP / Bottom-Up Row Transitions

Time Complexity:  O(N^2) - Iterating each cell of N x N matrix
Space Complexity: O(1) auxiliary space if modified in-place
"""


class Solution:
    def maximumPath(self, n, mat):
        dp = [[0] * n for _ in range(n)]
        for c in range(n):
            dp[0][c] = mat[0][c]

        for r in range(1, n):
            for c in range(n):
                if c == 0:
                    dp[r][c] = mat[r][c] + max(dp[r - 1][c], dp[r - 1][c + 1])
                elif c == n - 1:
                    dp[r][c] = mat[r][c] + max(dp[r - 1][c], dp[r - 1][c - 1])
                else:
                    dp[r][c] = mat[r][c] + max(dp[r - 1][c], dp[r - 1][c - 1], dp[r - 1][c + 1])
        return max(dp[-1])


if __name__ == "__main__":
    matrix = [[348, 391], [618, 193]]
    print(f"Max path sum: {Solution().maximumPath(len(matrix), matrix)}")
