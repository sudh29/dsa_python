"""
Problem: Friends Pairing Problem
Category: Dynamic Programming
Pattern: Fibonacci Variant: dp[i] = dp[i-1] + (i-1)*dp[i-2]

Time Complexity:  O(N) - Linear iteration up to N
Space Complexity: O(1) - State variables tracking previous two values
"""


class Solution:
    def countFriendsPairings(self, n):
        MOD = 10**9 + 7
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2]) % MOD
        return dp[n]


if __name__ == "__main__":
    n = 3
    print(f"Friends pairing ways for {n}: {Solution().countFriendsPairings(n)}")
