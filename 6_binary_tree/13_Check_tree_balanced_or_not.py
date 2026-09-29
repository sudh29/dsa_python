"""
Problem: Check Tree Balanced Or Not
Category: Binary Trees
Pattern: Tree Traversal (DFS / BFS)

Time Complexity:  O(N) - Visits each node once
Space Complexity: O(H) - Recursion stack bounded by tree height
"""


# Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        lh = self.isBalanced(root.left)
        if lh == 0:
            return False
        rh = self.isBalanced(root.right)
        if rh == 0:
            return False
        if abs(lh - rh) > 1:
            return False
        else:
            return max(lh, rh) + 1
