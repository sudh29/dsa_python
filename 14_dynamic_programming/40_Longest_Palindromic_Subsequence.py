"""
Problem: Longest Palindromic Subsequence
Category: Dynamic Programming
Pattern: 2D Interval DP / LCS with Reversed String

Time Complexity:  O(N^2) - 2D matrix computation
Space Complexity: O(N^2) - 2D DP array
"""


class Solution:
    def longestPalinSubseq(self, S):
        n = len(S)
        rev_S = S[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if S[i - 1] == rev_S[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]


if __name__ == "__main__":
    s = "bbbab"
    print(f"Longest palindromic subsequence of '{s}': {Solution().longestPalinSubseq(s)}")
