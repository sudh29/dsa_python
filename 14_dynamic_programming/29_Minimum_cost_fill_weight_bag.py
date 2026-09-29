"""
Problem: Minimum Cost to Fill Given Weight in a Bag
Category: Dynamic Programming
Pattern: Unbounded Knapsack / Min-Cost DP

Time Complexity:  O(N * W) - Evaluating package sizes up to weight W
Space Complexity: O(W) - 1D DP table storage
"""

from typing import List


class Solution:
    def minimumCost(self, n: int, w: int, cost: List[int]) -> int:
        dp = [float("inf")] * (w + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if cost[i - 1] != -1:
                for j in range(i, w + 1):
                    dp[j] = min(dp[j], dp[j - i] + cost[i - 1])
        return dp[w] if dp[w] != float("inf") else -1


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, *args):
        return []

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    cost = [20, 10, 4, 50, 100]
    w = 5
    print(f"Min cost for weight {w}: {Solution().minimumCost(cost, len(cost), w)}")
