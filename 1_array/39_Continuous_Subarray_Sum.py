"""
Problem: Continuous Subarray Sum (LeetCode #523)
Pattern: Prefix Sum & Modulo Hash Map
Time Complexity: O(N)
Space Complexity: O(min(N, K))

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is defined as:
1. its length is at least two, and
2. the sum of the elements of the subarray is a multiple of k.
"""


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Determines whether a continuous subarray of length >= 2 exists with sum multiple of k.
        Uses prefix sum with remainder hash map. If (prefix_sum % k) was seen before at index
        i_prev such that (current_i - i_prev >= 2), then the subarray in between has sum divisible by k.
        """
        # Map: remainder -> earliest index seen
        remainder_map: dict[int, int] = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k if k != 0 else running_sum

            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Store only the earliest index to maximize the subarray length
                remainder_map[remainder] = i

        return False


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([23, 2, 4, 6, 7], 6, True),  # [2, 4] sums to 6
        ([23, 2, 6, 4, 7], 6, True),  # [23, 2, 6, 4, 7] sums to 42 (multiple of 6)
        ([23, 2, 6, 4, 7], 13, False),
        ([0, 0], 1, True),  # [0, 0] length 2, sums to 0
        ([5, 0, 0, 0], 3, True),  # [0, 0] sums to 0
        ([1, 0], 2, False),  # length 2, sums to 1
    ]

    for arr, k_val, expected in test_cases:
        result = sol.checkSubarraySum(arr, k_val)
        print(f"Nums: {arr}, k={k_val} => Result: {result} (Expected: {expected})")
        assert result == expected, (
            f"Failed for nums={arr}, k={k_val}: got {result}, expected {expected}"
        )

    print("All test cases passed!")
