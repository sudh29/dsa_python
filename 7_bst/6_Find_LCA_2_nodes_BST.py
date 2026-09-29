"""
Problem: Find Lca 2 Nodes Binary Search Tree
Category: Binary Search Trees
Pattern: Binary Search Tree Property (Left < Root < Right)

Time Complexity:  O(H) - O(log N) average, O(N) worst-case skewed tree
Space Complexity: O(1) iterative / O(H) recursive stack
"""


# Function to find the lowest common ancestor in a BST.
def LCA(root, n1, n2):
    if root is None:
        return None
    if root.data > n1 and root.data > n2:
        return LCA(root.left, n1, n2)
    if root.data < n1 and root.data < n2:
        return LCA(root.right, n1, n2)
    return root
