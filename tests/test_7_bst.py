"""Tests for 7_bst/ — BST Validation, Insertion, Deletion, AVL Rotations."""

import importlib
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common.tree_node import TreeNode


def _load(filename: str):
    """Dynamically imports a module from 7_bst/."""
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "7_bst" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestAVLTree:
    def test_insertion_and_balance(self):
        mod = _load("22_AVL_Tree_Self_Balancing.py")
        tree = mod.AVLTree()
        root = None
        for val in [10, 20, 30, 40, 50, 25]:
            root = tree.insert(root, val)

        inorder = tree.inorder(root)
        assert inorder == [10, 20, 25, 30, 40, 50], "Inorder must be sorted"

    def test_root_after_rotations(self):
        mod = _load("22_AVL_Tree_Self_Balancing.py")
        tree = mod.AVLTree()
        root = None
        for val in [10, 20, 30, 40, 50, 25]:
            root = tree.insert(root, val)
        assert root.val == 30, "Root should be 30 after AVL rebalancing"

    def test_preorder(self):
        mod = _load("22_AVL_Tree_Self_Balancing.py")
        tree = mod.AVLTree()
        root = None
        for val in [10, 20, 30, 40, 50, 25]:
            root = tree.insert(root, val)
        assert tree.preorder(root) == [30, 20, 10, 25, 40, 50]

    def test_single_insert(self):
        mod = _load("22_AVL_Tree_Self_Balancing.py")
        tree = mod.AVLTree()
        root = tree.insert(None, 42)
        assert root.val == 42
        assert tree.inorder(root) == [42]

    def test_right_left_case(self):
        """Triggers Right-Left rotation: insert 30, 50, 40."""
        mod = _load("22_AVL_Tree_Self_Balancing.py")
        tree = mod.AVLTree()
        root = None
        for val in [30, 50, 40]:
            root = tree.insert(root, val)
        assert tree.inorder(root) == [30, 40, 50]
        assert root.val == 40  # After RL rotation


class TestBSTValidation:
    def test_valid_bst(self):
        mod = _load("4_Check_if_tree_BST_or_not.py")
        sol = mod.Solution()
        # Valid BST: [4, 2, 6, 1, 3, 5, 7]
        root = TreeNode.from_level_order([4, 2, 6, 1, 3, 5, 7])
        assert sol.isBST(root) == 1

    def test_invalid_bst(self):
        mod = _load("4_Check_if_tree_BST_or_not.py")
        sol = mod.Solution()
        # Invalid: left child > root
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.right = TreeNode(1)
        assert sol.isBST(root) == 0
