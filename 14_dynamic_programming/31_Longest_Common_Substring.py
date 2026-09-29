"""
Problem: Longest Common Substring
Category: Dynamic Programming
Pattern: 2D Grid DP / Consecutive Match Resets

Time Complexity:  O(N * M) - Nested loop over characters of both strings
Space Complexity: O(N * M) - DP matrix storage
"""


class Solution:
    def longestCommonSubstr(self, str1, str2):
        n = len(str1)
        m = len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_len = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_len


if __name__ == "__main__":
    s1, s2 = "ABCDGH", "ACDGHR"
    print(f"Longest common substring: {Solution().longestCommonSubstr(s1, s2, len(s1), len(s2))}")
