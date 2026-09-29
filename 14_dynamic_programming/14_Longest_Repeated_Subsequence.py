"""
Problem: Longest Repeated Subsequence
Category: Dynamic Programming
Pattern: Memoization / Tabulation / Subproblem Overlap

Time Complexity:  O(N^2) / Polynomial
Space Complexity: O(N) - DP table storage
"""


class Solution:
    def LongestRepeatingSubsequence(self, s):
        def lrs_recursive(s, i, j, memo):
            if i == 0 or j == 0:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if s[i - 1] == s[j - 1] and i != j:
                memo[i][j] = 1 + lrs_recursive(s, i - 1, j - 1, memo)
            else:
                memo[i][j] = max(
                    lrs_recursive(s, i, j - 1, memo),
                    lrs_recursive(s, i - 1, j, memo),
                )
            return memo[i][j]

        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]


if __name__ == "__main__":
    s = "axxzxy"
    ob = Solution()
    print(ob.LongestRepeatingSubsequence(s))
