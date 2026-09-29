"""
Problem: Buy Maximum Stocks if i stocks can be bought on i-th day
Category: Greedy Algorithms
Pattern: Greedy Sort by Price / Greedy Quantity Pick

Time Complexity:  O(N log N) - Sorting price-day pairs
Space Complexity: O(N) - Storage for price-day pairs
"""

from typing import List


class Solution:
    def buyMaximumProducts(self, n: int, k: int, price: List[int]) -> int:
        data = [(price[i], i + 1) for i in range(n)]
        data.sort()
        res = 0
        for p, qty in data:
            if p * qty <= k:
                res += qty
                k -= p * qty
            else:
                res += k // p
                # k -= p * (k // p)
                break
        return res


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
    prices = [10, 7, 19]
    k = 45
    print(f"Max stocks with budget {k}: {Solution().buyMaximumProducts(len(prices), k, prices)}")
