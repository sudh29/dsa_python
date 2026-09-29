"""
Problem: Non Repeating Numbers
Category: Bit Manipulation
Pattern: XOR Accumulation & Rightmost Set Bit Partition

Time Complexity:  O(N) - Two passes over the array
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def singleNumber(self, nums):
        sums = 0
        for i in nums:
            sums = sums ^ i
        right_set_bit = sums & -sums
        x = 0
        y = 0
        for i in nums:
            if i & right_set_bit:
                x = x ^ i
            else:
                y = y ^ i

        if x < y:
            return [x, y]
        else:
            return [y, x]


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 1, 4]
    ob = Solution()
    print(ob.singleNumber(nums))  # Expected [3, 4]
