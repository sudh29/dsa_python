"""
Problem: Range Sum Query - Immutable (LeetCode #303)
Pattern: Prefix Sum (Difference Array / Range Queries)
Time Complexity: O(N) Precomputation, O(1) per Query
Space Complexity: O(N)

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
"""


class NumArray:
    """
    Data structure that supports O(1) range sum queries using 1D prefix sums.
    """

    def __init__(self, nums: list[int]):
        # prefix[i] stores the sum of nums[0...i-1]
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sumRange(self, left: int, right: int) -> int:
        """
        Returns sum of nums[left...right] in O(1) time.
        """
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)

    queries = [
        (0, 2, 1),  # (-2) + 0 + 3 = 1
        (2, 5, -1),  # 3 + (-5) + 2 + (-1) = -1
        (0, 5, -3),  # (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
    ]

    for left, right, expected in queries:
        result = obj.sumRange(left, right)
        print(f"sumRange({left}, {right}) => {result} (Expected: {expected})")
        assert result == expected, (
            f"Failed for range ({left}, {right}): got {result}, expected {expected}"
        )

    print("All test cases passed!")
