"""
Problem: Find The Median
Category: Arrays
Pattern: Two Pointers / Linear Scan

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def find_median(self, v):
        v.sort()
        n = len(v)
        if n % 2 == 0:
            return (v[n // 2] + v[(n // 2) - 1]) // 2
        else:
            return v[n // 2]
