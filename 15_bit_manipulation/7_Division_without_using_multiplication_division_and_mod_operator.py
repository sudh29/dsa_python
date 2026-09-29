"""
Problem: Division Without Using Multiplication Division And Mod Operator
Category: Bit Manipulation
Pattern: Bitwise AND / OR / XOR / Shift Tricks

Time Complexity:  O(1) / O(log N) - Proportional to number of bits
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def divide(self, a, b):
        # code here
        sign = -1 if ((a < 0) ^ (b < 0)) else 1
        # print(sign)
        a = abs(a)
        b = abs(b)
        q = 0
        temp = 0
        for i in range(31, -1, -1):
            if (temp + (b << i)) <= a:
                temp += b << i
                q |= 1 << i
        return -q if sign == -1 else q
