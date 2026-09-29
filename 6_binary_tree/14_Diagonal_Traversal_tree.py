"""
Problem: Diagonal Traversal Tree
Category: Binary Trees
Pattern: Tree Traversal (DFS / BFS)

Time Complexity:  O(N) - Visits each node once
Space Complexity: O(H) - Recursion stack bounded by tree height
"""


# Complete the function below
class Solution:
    def diagonal(self, root):
        if root is None:
            return
        res = []
        left_q = []
        node = root
        while node:
            res.append(node.data)
            if node.left:
                left_q.insert(0, node.left)

            if node.right:
                node = node.right
            else:
                node = left_q.pop() if left_q else None
        return res
