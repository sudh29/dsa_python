"""
Problem: Search Element in a Binary Tree
Category: Binary Trees
Pattern: Level-Order Traversal (BFS)

Time Complexity:  O(n) - Worst case visits all nodes
Space Complexity: O(w) - Where w is the maximum width of the tree (queue size)
"""

import sys
from collections import deque

sys.path.insert(0, ".")
from common.tree_node import TreeNode


def search_element(root: TreeNode | None, target: int) -> bool:
    """Searches for a target value in a binary tree using BFS.

    Args:
        root: Root of the binary tree.
        target: Value to search for.

    Returns:
        True if the target exists in the tree, False otherwise.
    """
    if not root:
        return False

    queue: deque[TreeNode] = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == target:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False


if __name__ == "__main__":
    root = TreeNode.from_level_order([2, 6, 8, 3, 1, 4, 2, 11, 4])
    assert root is not None

    assert search_element(root, 11) is True
    assert search_element(root, 81) is False
    assert search_element(root, 2) is True
    assert search_element(root, 6) is True
    assert search_element(None, 5) is False

    print("All search element demonstrations passed!")
