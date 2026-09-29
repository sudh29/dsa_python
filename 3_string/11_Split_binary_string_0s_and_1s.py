"""
Problem: Split Binary String 0S And 1S
Category: Strings
Pattern: Two Pointers / Sliding Window

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def maxSubStr(self, str):
        # Write your code here
        c1 = 0
        c0 = 0
        c = 0
        for i in str:
            if i == "0":
                c0 += 1
            elif i == "1":
                c1 += 1
            if c0 == c1:
                c += 1
        return c if c0 == c1 else -1
