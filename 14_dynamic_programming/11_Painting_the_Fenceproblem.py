"""
Problem: Painting the Fence
Category: Dynamic Programming
Pattern: State Reduction / Fibonacci Variant

Time Complexity:  O(N) - Single loop computing combinations modulo 10^9 + 7
Space Complexity: O(1) - Constant auxiliary space using state variables
"""


class Solution:
    def countWays(self, n, k):
        MOD = 10**9 + 7
        if n == 1:
            return k
        if n == 2:
            return k * k % MOD
        # dp = [0] * (n + 1)
        # dp[1] = k
        # dp[2] = k * k
        # for i in range(3, n + 1):
        #     dp[i] = (k - 1) * (dp[i-1] + dp[i-2]) % MOD
        # return dp[n]

        prev2 = k
        prev1 = k * k % MOD
        for i in range(3, n + 1):
            current = (k - 1) * (prev1 + prev2) % MOD
            prev2 = prev1
            prev1 = current
        return prev1


if __name__ == "__main__":
    n, k = 3, 2
    print(f"Ways to paint {n} posts with {k} colors: {Solution().countWays(n, k)}")
