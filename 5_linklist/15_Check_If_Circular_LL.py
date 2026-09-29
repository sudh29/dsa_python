"""
Problem: Check If Circular Linked List
Category: Linked Lists
Pattern: Pointer Manipulation / Fast & Slow Pointers

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


def isCircular(head):
    if head is None:
        return True
    curr = head
    while curr:
        if curr.next == head:
            return True
        curr = curr.next
    return False
