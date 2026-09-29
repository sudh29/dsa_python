"""
Problem: Find First Node Of Loop Linked List
Category: Linked Lists
Pattern: Floyd's Cycle-Finding Algorithm (Fast & Slow Pointers)

Time Complexity:  O(N) - Fast pointer catches slow pointer within one cycle
Space Complexity: O(1) - Two pointer variables
"""


class Solution:
    # Function to remove a loop in the linked list.
    def detectloopstarting(self, head):
        # code here
        # remove the loop without losing any nodes
        first = head
        second = head
        while first and second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                break
        if first != second:
            return None
        first = head
        while first != second:
            first = first.next
            second = second.next

        return first
