"""
Problem: Count Palindromic Subsequences
Category: Strings
Pattern: Dynamic Programming (2D Interval DP)

Time Complexity:  O(N^2) - Substring interval matrix filling
Space Complexity: O(N^2) - DP table for substring counts
"""

MOD = 10**9 + 7


def is_palindrome(s):
    return s == s[::-1]


class Solution:
    def countPS(self, S):
        # n = len(S)
        # count = 0

        # def generate_subsequences(S, index, current):
        #     nonlocal count
        #     if index == n:
        #         if current and is_palindrome(current):
        #             count += 1
        #         return
        #     generate_subsequences(S, index + 1, current + S[index])
        #     generate_subsequences(S, index + 1, current)

        # generate_subsequences(S, 0, "")
        # return count

        # DP solution
        n = len(S)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if S[i] == S[j]:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] + 1) % MOD
                else:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
        return dp[0][n - 1]


if __name__ == "__main__":
    ob = Solution()
    s = "abcd"
    print(f"Palindromic subsequences in '{s}': {ob.countPS(s)}")
