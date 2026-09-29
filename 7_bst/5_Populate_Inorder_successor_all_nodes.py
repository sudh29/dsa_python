"""
Problem: Populate Inorder Successor All Nodes
Category: Binary Search Trees
Pattern: BST Inorder / Divide & Conquer

Time Complexity:  O(H) where H is tree height
Space Complexity: O(H) - Recursion stack
"""


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


temp = Node(None)


class Solution:
    def populateNext(self, root):
        global temp
        if root is None:
            return
        self.populateNext(root.left)
        if temp is not None:
            temp.next = root
        temp = root
        self.populateNext(root.right)
