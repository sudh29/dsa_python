"""
Problem: Check If Tree Binary Search Tree Or Not
Category: Binary Search Trees
Pattern: Range Invalidation [min_val, max_val] DFS

Time Complexity:  O(N) - Checks each node satisfies BST invariant
Space Complexity: O(H) - Call stack
"""


class Solution:
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        temp = []

        def BST(root, temp):
            if root:
                BST(root.left, temp)
                temp.append(root.data)
                BST(root.right, temp)

        BST(root, temp)
        for i in range(1, len(temp)):
            if temp[i] <= temp[i - 1]:
                return False
        return True
