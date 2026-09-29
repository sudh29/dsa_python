"""
Problem: Maximum Sum Such That No 2 Elements Are Adjacent
Category: Searching & Sorting
Pattern: Binary Search / Divide & Conquer

Time Complexity:  O(N log N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    # Function to find the maximum money the thief can get.
    def FindMaxSum(self, arr, n):
        # Handle edge cases
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        # Initialize dp array
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        # Fill the dp array with maximum sums
        for i in range(2, n):
            dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])

        return dp[n - 1]
