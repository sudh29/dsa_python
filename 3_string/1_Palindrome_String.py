"""
Problem: Palindrome String
Category: Strings
Pattern: Two Pointers / Sliding Window

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def isPalindrome(self, S):
        n = len(S)
        for i in range(n // 2):
            if S[i] != S[n - i - 1]:
                return 0
        return 1
