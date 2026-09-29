"""
Problem: Container With Most Water (LeetCode #11)
Pattern: Two Pointers (Opposite Direction)
Time Complexity: O(N)
Space Complexity: O(1)

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Calculate maximum water that can be trapped between two vertical lines.
        Uses a two-pointer approach moving the smaller height inward.
        """
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Width between the two lines
            width = right - left
            # Container height is limited by the shorter line
            h = min(height[left], height[right])
            current_area = width * h
            max_water = max(max_water, current_area)

            # Move pointer with smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]

    for heights, expected in test_cases:
        result = sol.maxArea(heights)
        print(f"Height: {heights} => Max Area: {result} (Expected: {expected})")
        assert result == expected, (
            f"Failed for {heights}: got {result}, expected {expected}"
        )

    print("All test cases passed!")
