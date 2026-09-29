"""
Problem: Best Time To Buy And Sell Stock
Category: Arrays
Pattern: Two Pointers / Linear Scan

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_val = 100000
        for i in range(n):
            min_val = min(min_val, prices[i])
            max_profit = max(max_profit, prices[i] - min_val)
        return max_profit
