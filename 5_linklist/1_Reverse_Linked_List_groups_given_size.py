"""
Problem: Reverse Linked List Groups Given Size
Category: Linked Lists
Pattern: In-place Pointer Reversal

Time Complexity:  O(N) - Traverses list once reversing pointers
Space Complexity: O(1) - In-place pointer modifications
"""


class Solution:
    def reverse(self, head, k):
        curr = head
        prev = None
        nxt = None
        c = 0
        while curr and c < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            c += 1
        if nxt:
            head.next = self.reverse(nxt, k)
        return prev
