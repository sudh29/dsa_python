"""
Problem: Reverse Level Order Traversal
Category: Binary Trees
Pattern: Breadth-First Search (Queue / Level Order)

Time Complexity:  O(N) - Enqueues and dequeues each node once
Space Complexity: O(W) - Max width of the binary tree
"""


def reverseLevelOrder(root):
    # code here
    # Code here
    res = []
    queue = [root]
    while queue:
        value = queue.pop(0)
        res.append(value.data)
        if value.right:
            queue.append(value.right)
        if value.left:
            queue.append(value.left)
    return res[::-1]
