"""
Problem: Find Maximum Element in a Binary Tree
Category: Binary Trees
Pattern: Level-Order Traversal (BFS)

Time Complexity:  O(n) - Must visit every node to find the maximum
Space Complexity: O(w) - Where w is the maximum width of the tree (queue size)
"""

import sys
from collections import deque

sys.path.insert(0, ".")
from common.tree_node import TreeNode


def find_max_element(root: TreeNode | None) -> int | None:
    """Finds the maximum value element in a binary tree using BFS.

    Args:
        root: Root of the binary tree.

    Returns:
        The maximum value, or None if the tree is empty.
    """
    if not root:
        return None

    queue: deque[TreeNode] = deque([root])
    max_val = float("-inf")

    while queue:
        node = queue.popleft()
        if node.val > max_val:
            max_val = node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return int(max_val)


if __name__ == "__main__":
    # Tree:
    #       2
    #      / \
    #     6   8
    #    / \ / \
    #   3  1 4  2
    #  / \
    # 11  4
    root = TreeNode.from_level_order([2, 6, 8, 3, 1, 4, 2, 11, 4])
    assert root is not None
    assert find_max_element(root) == 11

    # Single node
    assert find_max_element(TreeNode(42)) == 42

    # Negative values
    root2 = TreeNode.from_level_order([-5, -3, -8])
    assert root2 is not None
    assert find_max_element(root2) == -3

    # Empty tree
    assert find_max_element(None) is None

    print("All find maximum element demonstrations passed!")
