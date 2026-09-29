"""
Problem: Subarray Sum Equals K (LeetCode #560)
Pattern: Prefix Sum & Hash Map
Time Complexity: O(N)
Space Complexity: O(N)

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Counts total number of contiguous subarrays whose sum equals k.
        Uses prefix sum with a frequency map: if prefix_sum - k was seen previously,
        the subarray between that previous index and current index sums to k.
        """
        prefix_counts: dict[int, int] = {0: 1}
        current_sum = 0
        total_subarrays = 0

        for num in nums:
            current_sum += num
            target = current_sum - k

            if target in prefix_counts:
                total_subarrays += prefix_counts[target]

            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

        return total_subarrays


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
        ([-1, -1, 1], 0, 1),
    ]

    for arr, k_val, expected in test_cases:
        result = sol.subarraySum(arr, k_val)
        print(
            f"Nums: {arr}, k={k_val} => Subarrays count: {result} (Expected: {expected})"
        )
        assert result == expected, (
            f"Failed for nums={arr}, k={k_val}: got {result}, expected {expected}"
        )

    print("All test cases passed!")
