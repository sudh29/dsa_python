"""
Problem: Mirror Of A Tree
Category: Binary Trees
Pattern: Recursive DFS Node Swapping

Time Complexity:  O(N) - Inverts left and right subtrees for every node
Space Complexity: O(H) - Call stack
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # if root is None:
        #     return root
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # root.left, root.right = root.right, root.left
        # return root

        if root is None:
            return
        q = []
        q.append(root)
        while len(q):
            curr = q[0]
            q.pop(0)
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root
