"""
Problem: Check If Linked List Is Palindrome
Category: Linked Lists
Pattern: Fast & Slow Pointers + Half-List Reversal

Time Complexity:  O(N) - Traversal and comparison
Space Complexity: O(1) - In-place reversal and restore
"""


class Solution:
    def isPalindrome(self, head):
        # code here
        temp = []
        curr = head
        while curr:
            temp.append(curr.data)
            curr = curr.next
        for i in range(int(len(temp) / 2)):
            if temp[i] != temp[len(temp) - 1 - i]:
                return False
        return True
