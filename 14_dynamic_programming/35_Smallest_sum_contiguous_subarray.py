"""
Problem: Smallest Sum Contiguous Subarray
Category: Dynamic Programming
Pattern: Kadane's Algorithm (Min Sum Variant)

Time Complexity:  O(N) - Single pass through the array
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def smallestSumSubarray(self, arr, n):
        # min_so_far = arr[0]
        # current_min = arr[0]
        # for i in range(1, n):
        #     current_min = min(arr[i], current_min + arr[i])
        #     min_so_far = min(min_so_far, current_min)
        # return min_so_far

        dp = [0] * n
        dp[0] = arr[0]
        min_sum = dp[0]
        for i in range(1, n):
            dp[i] = min(arr[i], dp[i - 1] + arr[i])
            min_sum = min(min_sum, dp[i])
        return min_sum


if __name__ == "__main__":
    arr = [3, -4, 2, -3, -1, 7, -5]
    print(f"Smallest contiguous sum: {Solution().smallestSumSubarray(arr, len(arr))}")
