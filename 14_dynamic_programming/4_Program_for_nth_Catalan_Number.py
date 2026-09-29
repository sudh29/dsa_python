"""
Problem: Program for nth Catalan Number
Category: Dynamic Programming
Pattern: Catalan Convolution DP

Time Complexity:  O(N^2) - Convolution sum over subproblems
Space Complexity: O(N) - 1D DP array storing Catalan numbers
"""


class Solution:
    def findCatalan(self, N: int) -> int:
        MOD = 1000000007
        dp = [0] * (N + 1)
        dp[0] = dp[1] = 1
        for i in range(2, N + 1):
            for j in range(i):
                dp[i] = (dp[i] + (dp[j] * dp[i - j - 1]) % MOD) % MOD
        return dp[N]


if __name__ == "__main__":
    n = 5
    print(f"Catalan number C({n}): {Solution().findCatalan(n)}")
