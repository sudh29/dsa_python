"""
Problem: Factorials Of Large Numbers
Category: Arrays
Pattern: Two Pointers / Linear Scan

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def factorial(self, N):
        # code here
        temp = 1
        while N > 0:
            temp *= N
            N -= 1
        temp = [int(i) for i in str(temp)]
        # print(temp)
        return temp
