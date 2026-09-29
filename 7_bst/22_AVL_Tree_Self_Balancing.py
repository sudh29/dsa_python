"""
Problem: AVL Tree (Self-Balancing Binary Search Tree)
Category: Binary Search Trees
Pattern: Self-Balancing BST with Rotations

Time Complexity:  O(log n) per insertion - Height is maintained at O(log n) via rotations
Space Complexity: O(n) - Storage for n nodes; O(log n) recursion stack per operation
"""


class AVLNode:
    """Node for an AVL tree with height tracking."""

    def __init__(self, val: int) -> None:
        self.val = val
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.height: int = 1


class AVLTree:
    """AVL Tree implementation with insertion and all four rotation cases.

    Maintains the BST property while ensuring the balance factor
    (|height(left) - height(right)|) never exceeds 1 for any node.
    """

    def _get_height(self, node: AVLNode | None) -> int:
        """Returns the height of a node (0 for None)."""
        return node.height if node else 0

    def _get_balance(self, node: AVLNode | None) -> int:
        """Returns the balance factor (left height - right height)."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, z: AVLNode) -> AVLNode:
        """Right rotation around node z."""
        y = z.left
        assert y is not None
        t2 = y.right

        y.right = z
        z.left = t2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z: AVLNode) -> AVLNode:
        """Left rotation around node z."""
        y = z.right
        assert y is not None
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def insert(self, root: AVLNode | None, key: int) -> AVLNode:
        """Inserts a key into the AVL tree and rebalances as needed.

        Handles all four imbalance cases:
        - Left-Left:  Single right rotation
        - Left-Right: Left rotation on left child, then right rotation
        - Right-Right: Single left rotation
        - Right-Left: Right rotation on right child, then left rotation
        """
        if not root:
            return AVLNode(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        # Left-Left case
        if balance > 1 and root.left and key < root.left.val:
            return self._rotate_right(root)

        # Left-Right case
        if balance > 1 and root.left and key > root.left.val:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right-Right case
        if balance < -1 and root.right and key > root.right.val:
            return self._rotate_left(root)

        # Right-Left case
        if balance < -1 and root.right and key < root.right.val:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def preorder(self, root: AVLNode | None) -> list[int]:
        """Returns the preorder traversal of the AVL tree."""
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def inorder(self, root: AVLNode | None) -> list[int]:
        """Returns the inorder traversal (sorted order) of the AVL tree."""
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


if __name__ == "__main__":
    tree = AVLTree()
    root = None

    for val in [10, 20, 30, 40, 50, 25]:
        root = tree.insert(root, val)

    preorder = tree.preorder(root)
    inorder = tree.inorder(root)

    # AVL tree should be balanced — inorder must be sorted
    assert inorder == [10, 20, 25, 30, 40, 50], f"Inorder failed: {inorder}"

    # Root should be 30 after all rotations
    assert root is not None
    assert root.val == 30, f"Root should be 30 after balancing, got {root.val}"

    # Verify preorder matches expected balanced structure
    assert preorder == [30, 20, 10, 25, 40, 50], f"Preorder failed: {preorder}"

    print("All AVL tree demonstrations passed!")
