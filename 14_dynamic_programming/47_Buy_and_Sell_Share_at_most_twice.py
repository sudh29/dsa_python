"""
Problem: Buy and Sell Share at Most Twice
Category: Dynamic Programming
Pattern: Prefix and Suffix Profit Arrays / State DP

Time Complexity:  O(N) - Two passes computing left and right maximum profits
Space Complexity: O(N) - Auxiliary profit array
"""

from typing import List


class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        if n == 0:
            return 0
        left_profit = [0] * n
        right_profit = [0] * n
        min_price = price[0]
        for i in range(1, n):
            min_price = min(min_price, price[i])
            left_profit[i] = max(left_profit[i - 1], price[i] - min_price)
        max_price = price[n - 1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, price[i])
            right_profit[i] = max(right_profit[i + 1], max_price - price[i])
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profit[i] + right_profit[i])
        return max_profit


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
    prices = [10, 22, 5, 75, 65, 80]
    print(f"Max profit with <= 2 transactions: {Solution().maxProfit(len(prices), prices)}")
