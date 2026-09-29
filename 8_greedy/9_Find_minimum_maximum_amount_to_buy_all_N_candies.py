"""
Problem: Find Minimum and Maximum Amount to Buy All N Candies
Category: Greedy Algorithms
Pattern: Sorting / Two Pointers / Free Candy Greed

Time Complexity:  O(N log N) - Sorting candy prices
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def candyStore(self, candies, N, K):
        min_val = 0
        max_val = 0
        candies.sort()
        j = N - 1
        m = 0
        n = N - 1
        for i in range(N):
            if i <= j:
                min_val += candies[i]
                j -= K
            if m <= n:
                max_val += candies[n]
                m += K
                n -= 1

        return min_val, max_val


if __name__ == "__main__":
    candies = [3, 2, 1, 4]
    k = 2
    print(f"Min and max cost with {k} free: {Solution().candyStore(candies, len(candies), k)}")
