"""
Problem: Count Balanced Binary Trees of Height H
Category: Dynamic Programming
Pattern: Fibonacci Variant / Modular Arithmetic

Time Complexity:  O(H) - Linear iteration up to height H
Space Complexity: O(H) - DP array for tree counts
"""


class Solution:
    def countBT(self, h):
        MOD = 10**9 + 7
        if h == 0 or h == 1:
            return 1
        dp = [0] * (h + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, h + 1):
            dp[i] = (dp[i - 1] * dp[i - 1] + 2 * dp[i - 1] * dp[i - 2]) % MOD
        return dp[h]


if __name__ == "__main__":
    h = 3
    print(f"Balanced binary trees of height {h}: {Solution().countBT(h)}")
