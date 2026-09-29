"""
Problem: Majority Element Ii K N
Category: Arrays
Pattern: Two Pointers / Linear Scan

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        temp = set()
        k = len(nums) // 3
        dictemp = {}
        for i in nums:
            if i not in dictemp:
                dictemp[i] = 1
            else:
                dictemp[i] += 1
        for i in nums:
            if dictemp[i] > k:
                temp.add(i)
        return temp
