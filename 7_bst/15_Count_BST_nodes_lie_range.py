"""
Problem: Count Binary Search Tree Nodes Lie Range
Category: Binary Search Trees
Pattern: BST Inorder / Divide & Conquer

Time Complexity:  O(H) where H is tree height
Space Complexity: O(H) - Recursion stack
"""


# Function to count number of nodes in BST that lie in the given range.
class Solution:
    def inorder(self, root, ans):
        if root is None:
            return
        self.inorder(root.left, ans)
        ans.append(root.data)
        self.inorder(root.right, ans)

    def getCount(self, root, low, high):
        if root is None:
            return 0
        res = []
        self.inorder(root, res)
        count = 0
        for i in res:
            if i >= low and i <= high:
                count += 1
        return count
