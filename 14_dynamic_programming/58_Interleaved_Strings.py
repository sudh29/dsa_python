"""
Problem: Interleaved Strings
Category: Dynamic Programming
Pattern: 2D Grid DP / String Matching

Time Complexity:  O(N * M) - DP matrix filling of prefix interleavings
Space Complexity: O(N * M) - 2D boolean DP array
"""


class Solution:
    # function should return True/False
    def isInterleave(self, A, B, C):
        n, m, k = len(A), len(B), len(C)
        if n + m != k:
            return False
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and B[j - 1] == C[j - 1]
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] and A[i - 1] == C[i - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (dp[i - 1][j] and A[i - 1] == C[i + j - 1]) or (
                    dp[i][j - 1] and B[j - 1] == C[i + j - 1]
                )
        return dp[n][m]


if __name__ == "__main__":
    a, b, c = "aabcc", "dbbca", "aadbbcbcac"
    print(f"Is '{c}' interleaved from '{a}' and '{b}': {Solution().isInterleave(a, b, c)}")
