"""
Problem: Coin Change - Number of Ways
Category: Dynamic Programming
Pattern: Unbounded Knapsack / 1D DP

Time Complexity:  O(N * Sum) - Iterating coins and filling DP array
Space Complexity: O(Sum) - 1D DP array storage
"""


class Solution:
    def count(self, coins, N, Sum):
        dp = [0] * (Sum + 1)
        dp[0] = 1
        for coin in coins:
            for amount in range(coin, Sum + 1):
                dp[amount] += dp[amount - coin]
        return dp[Sum]


if __name__ == "__main__":
    coins = [1, 2, 3]
    total = 4
    print(f"Ways to make sum {total} with {coins}: {Solution().count(coins, len(coins), total)}")
