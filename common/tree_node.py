"""
Problem: Tree Node
Category: Algorithms
Pattern: Algorithmic Pattern

Time Complexity:  O(N)
Space Complexity: O(1)
"""

from collections import deque
from typing import Any, Self


class TreeNode:
    """Standard binary tree node supporting .val, .data, .left, and .right."""

    def __init__(
        self,
        val: int = 0,
        left: Self | None = None,
        right: Self | None = None,
    ) -> None:
        self.val = val
        self.data = val  # Compatibility alias
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TreeNode):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

    @classmethod
    def from_level_order(cls, values: list[int | None]) -> Self | None:
        """Constructs a binary tree from a LeetCode-style level order list."""
        if not values or values[0] is None:
            return None

        root = cls(values[0])
        queue: deque[TreeNode] = deque([root])
        idx = 1
        n = len(values)

        while queue and idx < n:
            curr = queue.popleft()

            # Left child
            if idx < n and values[idx] is not None:
                val = values[idx]
                assert val is not None
                curr.left = cls(val)
                queue.append(curr.left)
            idx += 1

            # Right child
            if idx < n and values[idx] is not None:
                val = values[idx]
                assert val is not None
                curr.right = cls(val)
                queue.append(curr.right)
            idx += 1

        return root

    def to_level_order(self) -> list[int | None]:
        """Serializes the binary tree into a level-order list."""
        res: list[int | None] = []
        queue: deque[TreeNode | None] = deque([self])

        while queue:
            curr = queue.popleft()
            if curr is not None:
                res.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append(None)

        # Trim trailing None values
        while res and res[-1] is None:
            res.pop()

        return res
