"""
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""


class Solution:
    def toSumTree(self, root):
        if root is None:
            return 0
        old_root_data = root.data
        root.data = self.toSumTree(root.left) + self.toSumTree(root.right)
        return old_root_data + root.data
