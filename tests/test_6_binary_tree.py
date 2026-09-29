"""Tests for 6_binary_tree/ — Traversals, Views, LCA, Diameter."""

import importlib
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common.tree_node import TreeNode


def _load(filename: str):
    """Dynamically imports a module from 6_binary_tree/."""
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "6_binary_tree" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestTreeHeight:
    def test_balanced_tree(self, sample_tree):
        mod = _load("2_Height_of_a_tree.py")
        sol = mod.Solution()
        assert sol.height(sample_tree) == 3

    def test_single_node(self):
        mod = _load("2_Height_of_a_tree.py")
        sol = mod.Solution()
        assert sol.height(TreeNode(1)) == 1

    def test_skewed(self, skewed_tree):
        mod = _load("2_Height_of_a_tree.py")
        sol = mod.Solution()
        assert sol.height(skewed_tree) == 4


class TestTreeDiameter:
    def test_balanced_tree(self, sample_tree):
        mod = _load("3_Diameter_of_a_tree.py")
        sol = mod.Solution()
        # Diameter of balanced [1,2,3,4,5,6,7] = 5 (path 4→2→1→3→7 or similar)
        assert sol.diameter(sample_tree) == 5

    def test_single_node(self):
        mod = _load("3_Diameter_of_a_tree.py")
        sol = mod.Solution()
        assert sol.diameter(TreeNode(1)) == 1

    def test_linear(self, skewed_tree):
        mod = _load("3_Diameter_of_a_tree.py")
        sol = mod.Solution()
        assert sol.diameter(skewed_tree) == 4


class TestReverseLevelOrder:
    def test_balanced_tree(self, sample_tree):
        mod = _load("1_Reverse_Level_Order_traversal.py")
        result = mod.reverseLevelOrder(sample_tree)
        # Algorithm enqueues right before left, then reverses the list
        assert result == [4, 5, 6, 7, 2, 3, 1]

    def test_single_node(self):
        mod = _load("1_Reverse_Level_Order_traversal.py")
        result = mod.reverseLevelOrder(TreeNode(42))
        assert result == [42]


class TestMaxLevelSum:
    def test_basic(self):
        mod = _load("35_Maximum_Level_Sum_Binary_Tree.py")
        root = TreeNode.from_level_order([1, 7, 0, 7, -8])
        assert mod.max_level_sum(root) == 1

    def test_single_node(self):
        mod = _load("35_Maximum_Level_Sum_Binary_Tree.py")
        assert mod.max_level_sum(TreeNode(42)) == 0


class TestFindMaxElement:
    def test_basic(self):
        mod = _load("36_Find_Maximum_Element_Binary_Tree.py")
        root = TreeNode.from_level_order([2, 6, 8, 3, 1, 4, 2, 11, 4])
        assert mod.find_max_element(root) == 11

    def test_empty(self):
        mod = _load("36_Find_Maximum_Element_Binary_Tree.py")
        assert mod.find_max_element(None) is None

    def test_negative(self):
        mod = _load("36_Find_Maximum_Element_Binary_Tree.py")
        root = TreeNode.from_level_order([-5, -3, -8])
        assert mod.find_max_element(root) == -3


class TestSearchElement:
    def test_found(self):
        mod = _load("37_Search_Element_Binary_Tree.py")
        root = TreeNode.from_level_order([2, 6, 8, 3, 1, 4, 2, 11, 4])
        assert mod.search_element(root, 11) is True

    def test_not_found(self):
        mod = _load("37_Search_Element_Binary_Tree.py")
        root = TreeNode.from_level_order([2, 6, 8, 3, 1, 4, 2, 11, 4])
        assert mod.search_element(root, 99) is False

    def test_empty_tree(self):
        mod = _load("37_Search_Element_Binary_Tree.py")
        assert mod.search_element(None, 5) is False
