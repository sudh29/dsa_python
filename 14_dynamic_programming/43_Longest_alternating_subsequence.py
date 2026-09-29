"""
Problem: Longest Alternating Subsequence
Category: Dynamic Programming
Pattern: Greedy Peak-Valley Counting / State Tracking

Time Complexity:  O(N) - Single pass updating inc and dec states
Space Complexity: O(1) auxiliary space
"""


class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        if not arr:
            return 0
        n = len(arr)
        up = 1
        down = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
        return max(up, down)


if __name__ == "__main__":
    nums = [1, 5, 4]
    print(f"Longest alternating subsequence: {Solution().AlternatingaMaxLength(nums)}")
