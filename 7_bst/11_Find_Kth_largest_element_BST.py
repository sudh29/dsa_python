"""
Problem: Find Kth Largest Element Binary Search Tree
Category: Binary Search Trees
Pattern: Binary Search Tree Property (Left < Root < Right)

Time Complexity:  O(H) - O(log N) average, O(N) worst-case skewed tree
Space Complexity: O(1) iterative / O(H) recursive stack
"""

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None


# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self, root, k):
        def kth(node):
            nonlocal k, result
            if node is None or k == 0:
                return
            kth(node.right)
            k -= 1
            if k == 0:
                result = node.data
            kth(node.left)

        result = None
        kth(root)
        return result
