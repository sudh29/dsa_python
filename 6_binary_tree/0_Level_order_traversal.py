"""
Problem: Level Order Traversal
Category: Binary Trees
Pattern: Breadth-First Search (Queue / Level Order)

Time Complexity:  O(N) - Enqueues and dequeues each node once
Space Complexity: O(W) - Max width of the binary tree
"""


class Solution:
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        # Code here
        res = []
        queue = [root]
        while queue:
            value = queue.pop(0)
            res.append(value.data)
            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)
        return res
