"""Tests for common/ — Shared data structure utilities."""

import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common.graph_node import DisjointSetUnion, GraphNode
from common.list_node import DoublyListNode, ListNode
from common.tree_node import TreeNode
from common.trie_node import TrieNode


class TestListNode:
    def test_from_list(self):
        head = ListNode.from_list([1, 2, 3])
        assert head is not None
        assert head.to_list() == [1, 2, 3]

    def test_empty_list(self):
        assert ListNode.from_list([]) is None

    def test_single_node(self):
        head = ListNode.from_list([42])
        assert head is not None
        assert head.val == 42
        assert head.data == 42  # GfG compatibility
        assert head.next is None

    def test_equality(self):
        a = ListNode.from_list([1, 2, 3])
        b = ListNode.from_list([1, 2, 3])
        assert a == b

    def test_inequality(self):
        a = ListNode.from_list([1, 2])
        b = ListNode.from_list([1, 3])
        assert a != b

    def test_repr(self):
        node = ListNode(5)
        assert repr(node) == "ListNode(5)"


class TestDoublyListNode:
    def test_from_list(self):
        head = DoublyListNode.from_list([1, 2, 3])
        assert head is not None
        assert head.to_list() == [1, 2, 3]

    def test_prev_pointers(self):
        head = DoublyListNode.from_list([1, 2, 3])
        assert head.next.prev == head  # type: ignore[union-attr]
        assert head.next.next.prev == head.next  # type: ignore[union-attr]

    def test_empty_list(self):
        assert DoublyListNode.from_list([]) is None


class TestTreeNode:
    def test_from_level_order(self):
        root = TreeNode.from_level_order([1, 2, 3, 4, 5])
        assert root is not None
        assert root.val == 1
        assert root.left.val == 2  # type: ignore[union-attr]
        assert root.right.val == 3  # type: ignore[union-attr]

    def test_to_level_order_roundtrip(self):
        values = [1, 2, 3, None, 5, 6]
        root = TreeNode.from_level_order(values)
        assert root is not None
        result = root.to_level_order()
        assert result == [1, 2, 3, None, 5, 6]

    def test_empty(self):
        assert TreeNode.from_level_order([]) is None
        assert TreeNode.from_level_order([None]) is None

    def test_equality(self):
        a = TreeNode.from_level_order([1, 2, 3])
        b = TreeNode.from_level_order([1, 2, 3])
        assert a == b

    def test_data_alias(self):
        node = TreeNode(42)
        assert node.data == 42


class TestGraphNode:
    def test_creation(self):
        node = GraphNode(1)
        assert node.val == 1
        assert node.neighbors == []

    def test_with_neighbors(self):
        n1 = GraphNode(1)
        n2 = GraphNode(2)
        n1.neighbors.append(n2)
        assert len(n1.neighbors) == 1
        assert n1.neighbors[0].val == 2


class TestDisjointSetUnion:
    def test_union_find(self):
        dsu = DisjointSetUnion(5)
        assert dsu.union(0, 1) is True
        assert dsu.union(2, 3) is True
        assert dsu.find(0) == dsu.find(1)
        assert dsu.find(2) == dsu.find(3)
        assert dsu.find(0) != dsu.find(2)

    def test_redundant_union(self):
        dsu = DisjointSetUnion(3)
        assert dsu.union(0, 1) is True
        assert dsu.union(0, 1) is False  # Already in same set

    def test_transitive(self):
        dsu = DisjointSetUnion(4)
        dsu.union(0, 1)
        dsu.union(1, 2)
        assert dsu.find(0) == dsu.find(2)


class TestTrieNode:
    def test_creation(self):
        node = TrieNode()
        assert node.children == {}
        assert node.is_end_of_word is False
        assert node.count == 0
