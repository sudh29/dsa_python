"""
Problem: Largest Sum Contiguous Subarray (Kadane's Algorithm)
Category: Dynamic Programming
Pattern: Kadane's Algorithm / Prefix Tracking

Time Complexity:  O(N) - Single pass through the array
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def maxSubArraySum(self, arr):
        max_so_far = arr[0]
        current_max = arr[0]
        for i in range(1, len(arr)):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)
        return max_so_far


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Max contiguous sum: {Solution().maxSubArraySum(arr)}")
