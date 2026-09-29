"""
Problem: Set All The Bits In Given Range Of A Number
Category: Bit Manipulation
Pattern: Bitwise AND / OR / XOR / Shift Tricks

Time Complexity:  O(1) / O(log N) - Proportional to number of bits
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def setAllRangeBits(self, N, L, R):
        # code here
        mask = 0
        for i in range(L, R + 1):
            temp = 1 << (i - 1)
            mask = mask | temp
        return N | mask
