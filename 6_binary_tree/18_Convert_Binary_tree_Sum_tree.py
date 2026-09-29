"""
Problem: Convert Binary Tree Sum Tree
Category: Binary Trees
Pattern: Tree Traversal (DFS / BFS)

Time Complexity:  O(N) - Visits each node once
Space Complexity: O(H) - Recursion stack bounded by tree height
"""


class Solution:
    def toSumTree(self, root):
        if root is None:
            return 0
        old_root_data = root.data
        root.data = self.toSumTree(root.left) + self.toSumTree(root.right)
        return old_root_data + root.data
