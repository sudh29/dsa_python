"""
Problem: Binomial Coefficient (nCr % MOD)
Category: Dynamic Programming
Pattern: Pascal's Triangle / 1D DP

Time Complexity:  O(N * R) - DP table filling modulo 10^9 + 7
Space Complexity: O(R) - 1D DP array space
"""

MOD = 10**9 + 7


class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        dp = [0] * (r + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(min(i, r), 0, -1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD
        return dp[r]


if __name__ == "__main__":
    n, r = 5, 2
    print(f"C({n}, {r}) % MOD: {Solution().nCr(n, r)}")
