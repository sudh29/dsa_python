"""
Problem: Deletion And Reverse Linked List
Category: Linked Lists
Pattern: In-place Pointer Reversal

Time Complexity:  O(N) - Traverses list once reversing pointers
Space Complexity: O(1) - In-place pointer modifications
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to delete a given node from the list
def deleteNode(head, key):
    # your code goes here
    curr = head
    while curr.next.data != key:
        curr = curr.next
    curr.next = curr.next.next


# Function to reverse the list
def reverse(temp_head):
    # your code goes here
    newhead = temp_head
    curr = temp_head
    while curr.next != newhead:
        curr = curr.next
    curr.next = None
    newhead = temp_head
    curr = temp_head
    prev = None
    next = None
    while curr.next:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    curr.next = prev
    temp_head.next = curr
    global head
    head = curr
