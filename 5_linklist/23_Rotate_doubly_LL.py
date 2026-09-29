"""
Problem: Rotate Doubly Linked List
Category: Linked Lists
Pattern: Pointer Manipulation / Fast & Slow Pointers

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def rotateDLL(self, start, p):
        first = start
        second = start
        for i in range(p):
            first = first.next

        first.prev.next = None
        first.prev = None
        curr = first
        while curr.next:
            curr = curr.next

        curr.next = second
        second.prev = curr
        return first
