"""
Problem: Nth Node From End Of Linked List
Category: Linked Lists
Pattern: Pointer Manipulation / Fast & Slow Pointers

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


def getNthFromLast(head, n):
    slow = head
    fast = head
    for _ in range(1, n):
        if fast and fast.next is not None:
            fast = fast.next
        else:
            return -1
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    return slow.data if slow else -1
