"""
Problem: LCS of Three Strings
Category: Dynamic Programming
Pattern: 3D Dynamic Programming

Time Complexity:  O(N1 * N2 * N3) - Filling 3D DP array
Space Complexity: O(N1 * N2 * N3) - 3D DP table storage
"""


class Solution:
    def LCSof3(self, A, B, C, n1, n2, n3):
        dp = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                for k in range(1, n3 + 1):
                    if A[i - 1] == B[j - 1] == C[k - 1]:
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
        return dp[n1][n2][n3]


if __name__ == "__main__":
    a, b, c = "geeks", "geeksfor", "geeksforgeeks"
    print(f"LCS of three strings: {Solution().LCSof3(a, b, c, len(a), len(b), len(c))}")
