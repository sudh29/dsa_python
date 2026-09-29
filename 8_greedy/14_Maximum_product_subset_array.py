"""
Problem: Maximum Product Subset of an Array
Category: Greedy Algorithms
Pattern: Greedy Product / Negative Count Parity

Time Complexity:  O(N) - Single pass through the array
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def findMaxProduct(self, a, n):
        if n == 1:
            return a[0]
        mod = 10**9 + 7
        zero_count = 0
        negative_count = 0
        prod = 1
        max_negative = float("-inf")
        for i in a:
            if i == 0:
                zero_count += 1
                continue
            if i < 0:
                negative_count += 1
                max_negative = max(max_negative, i)
            prod = (prod * i) % mod

        if zero_count == n or (negative_count == 1 and negative_count + zero_count == n):
            return 0
        if negative_count % 2 != 0:
            prod = (prod * pow(max_negative, mod - 2, mod)) % mod
        return prod


if __name__ == "__main__":
    arr = [-1, -1, -2, 4, 3]
    print(f"Max product subset of {arr}: {Solution().findMaxProduct(arr, len(arr))}")
