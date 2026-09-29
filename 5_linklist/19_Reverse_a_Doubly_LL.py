"""
Problem: Reverse A Doubly Linked List
Category: Linked Lists
Pattern: In-place Pointer Reversal

Time Complexity:  O(N) - Traverses list once reversing pointers
Space Complexity: O(1) - In-place pointer modifications
"""


def reverseDLL(head):
    # return head after
    if head is None or head.next is None:
        return head
    curr = head
    while curr.next:
        curr = curr.next
    head = curr
    while curr:
        next = curr.next
        curr.next = curr.prev
        curr.prev = next
        curr = curr.next
    return head
