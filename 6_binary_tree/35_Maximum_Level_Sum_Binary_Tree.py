"""
Problem: Maximum Level Sum of a Binary Tree
Category: Binary Trees
Pattern: Level-Order Traversal (BFS) with Level Tracking
Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Time Complexity:  O(n) - Each node visited exactly once during BFS
Space Complexity: O(w) - Where w is the maximum width of the tree (queue size)
"""

import sys
from collections import deque

sys.path.insert(0, ".")
from common.tree_node import TreeNode


def max_level_sum(root: TreeNode | None) -> int:
    """Finds the level with the maximum sum in a binary tree.

    Args:
        root: Root of the binary tree.

    Returns:
        The 0-indexed level number with the maximum sum.
    """
    if not root:
        return -1

    queue: deque[TreeNode] = deque([root])
    max_sum = float("-inf")
    max_level = 0
    level = 0

    while queue:
        level_size = len(queue)
        current_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            current_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if current_sum > max_sum:
            max_sum = current_sum
            max_level = level

        level += 1

    return max_level


if __name__ == "__main__":
    # Tree:
    #       2
    #      / \
    #     6   8
    #    / \ / \
    #   3  1 4  2
    #  / \
    # 19  4
    root = TreeNode.from_level_order([2, 6, 8, 3, 1, 4, 2, 19, 4])
    assert root is not None
    assert max_level_sum(root) == 2, "Level 2 (3+1+4+2=10) should have max sum"

    # Simple tree
    root2 = TreeNode.from_level_order([1, 7, 0, 7, -8])
    assert root2 is not None
    assert max_level_sum(root2) == 1, "Level 1 (7+0=7) should have max sum"

    # Single node
    root3 = TreeNode(42)
    assert max_level_sum(root3) == 0

    print("All maximum level sum demonstrations passed!")
