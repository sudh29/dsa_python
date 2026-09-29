"""
Problem: Find Position Of The Only Set Bit
Category: Bit Manipulation
Pattern: Brian Kernighan's Algorithm: n = n & (n - 1)

Time Complexity:  O(k) where k is the number of set bits
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def findPosition(self, N):
        # code here
        """temp=bin(N)[2:]
        if temp.count('1')==1:
            val=len(temp)-temp.index('1')
            return val
        else:
            return -1"""
        c = 0
        index = 0
        temp = 0
        while N >= 1:
            # print(N)
            if N % 2 != 0:
                c += 1
            index += 1
            N = N // 2
            if c == 1:
                temp = index
        if c == 1:
            return temp
        else:
            return -1
