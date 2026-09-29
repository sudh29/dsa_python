"""
Problem: Maximum Sum Increasing Subsequence
Category: Dynamic Programming
Pattern: LIS DP Variant

Time Complexity:  O(N^2) - Nested loop comparing prefix elements
Space Complexity: O(N) - 1D DP array storing max sums
"""


class Solution:
    def maxSumIS(self, arr, n):
        dp = arr[:]
        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + arr[i])
        return max(dp)


if __name__ == "__main__":
    arr = [1, 101, 2, 3, 100, 4, 5]
    print(f"Max sum increasing subsequence of {arr}: {Solution().maxSumIS(arr, len(arr))}")
