"""
Problem: Reverse A Linked List
Category: Linked Lists
Pattern: In-place Pointer Reversal

Time Complexity:  O(N) - Traverses list once reversing pointers
Space Complexity: O(1) - In-place pointer modifications
"""


class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head


#     recursion
#     def reverse(node):
#     if (node == None):
#         return node

#     if (node.next == None):
#         return node

#     node1 = reverse(node.next)
#     node.next.next = node
#     node.next = None
#     return node1
