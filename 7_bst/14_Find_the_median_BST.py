"""
Problem: Find The Median Binary Search Tree
Category: Binary Search Trees
Pattern: Binary Search Tree Property (Left < Root < Right)

Time Complexity:  O(H) - O(log N) average, O(N) worst-case skewed tree
Space Complexity: O(1) iterative / O(H) recursive stack
"""


def inorder(node, res):
    if node is None:
        return
    inorder(node.left, res)
    res.append(node.data)
    inorder(node.right, res)


def findMedian(root):
    r1 = []
    inorder(root, r1)
    n = len(r1)
    mid = n // 2
    if n % 2 != 0:
        return r1[mid]
    val = (r1[mid] + r1[mid - 1]) / 2
    return int(val) if int(val) == val else val
