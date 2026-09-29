"""
Problem: Detect Loop In Linked List
Category: Linked Lists
Pattern: Floyd's Cycle-Finding Algorithm (Fast & Slow Pointers)

Time Complexity:  O(N) - Fast pointer catches slow pointer within one cycle
Space Complexity: O(1) - Two pointer variables
"""


class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # code here
        first = head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False
