"""
Problem: Find Kth Smallest Element Binary Search Tree
Category: Binary Search Trees
Pattern: Binary Search Tree Property (Left < Root < Right)

Time Complexity:  O(H) - O(log N) average, O(N) worst-case skewed tree
Space Complexity: O(1) iterative / O(H) recursive stack
"""


class Solution:
    # Return the Kth smallest element in the given BST
    def KthSmallestElement(self, root, k):
        def kth(node):
            nonlocal k, res
            if node is None or k == 0:
                return
            kth(node.left)
            k -= 1
            if k == 0:
                res = node.data
            kth(node.right)

        res = -1
        kth(root)
        return res
