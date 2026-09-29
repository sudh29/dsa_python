"""
Problem: Strings Are Rotations Of Other
Category: Strings
Pattern: Two Pointers / Sliding Window

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return 0
        temp = s1 + s1
        if s2 in temp:
            return 1
        return 0
