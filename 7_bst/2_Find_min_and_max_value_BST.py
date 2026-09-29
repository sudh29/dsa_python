"""
Problem: Find Min And Max Value Binary Search Tree
Category: Binary Search Trees
Pattern: Binary Search Tree Property (Left < Root < Right)

Time Complexity:  O(H) - O(log N) average, O(N) worst-case skewed tree
Space Complexity: O(1) iterative / O(H) recursive stack
"""


# Function to find the minimum element in the given BST.
def minValue(root):
    # if root is None:
    #     return -1
    # else:
    #     if root.left:
    #         return minValue(root.left)
    #     else:
    #         return root.data

    if root is None:
        return -1
    q = [root]
    while q:
        curr = q.pop()
        if curr.left:
            q.append(curr.left)
        else:
            return curr.data
    return curr.data
