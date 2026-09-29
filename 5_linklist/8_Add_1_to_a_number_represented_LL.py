"""
Problem: Add 1 To A Number Represented Linked List
Category: Linked Lists
Pattern: Pointer Manipulation / Fast & Slow Pointers

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def addOne(self, head):
        # Returns new head of linked List.
        curr = head
        s = ""
        while curr:
            s += str(curr.data)
            curr = curr.next
        s = str(int(s) + 1)
        curr = head
        prev = None
        for i in s:
            if curr:
                curr.data = int(i)
                prev = curr
                curr = curr.next
            else:
                curr = Node(int(i))
                prev.next = curr
                curr = curr.next
        return head
