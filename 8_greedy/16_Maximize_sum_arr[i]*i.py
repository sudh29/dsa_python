"""
Problem: Maximize sum of arr[i]*i
Category: Greedy Algorithms
Pattern: Greedy Sorting / Rearrangement Inequality

Time Complexity:  O(N log N) - Sorting array in non-decreasing order
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def Maximize(self, a, n):
        # Complete the function
        mod = 10**9 + 7
        a.sort()
        sum_total = 0
        for i in range(n):
            sum_total = (sum_total + a[i] * i) % mod
        return sum_total


if __name__ == "__main__":
    arr = [5, 3, 2, 4, 1]
    print(f"Maximized sum: {Solution().Maximize(arr, len(arr))}")
