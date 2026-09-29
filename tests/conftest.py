"""Shared fixtures and helpers for the dsa_python test suite."""

import sys
from pathlib import Path

import pytest

# Ensure the project root is on sys.path so that `common` and topic modules
# can be imported without installation.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.list_node import ListNode  # noqa: E402
from common.tree_node import TreeNode  # noqa: E402


# ─── Tree Fixtures ─────────────────────────────────────────────────────


@pytest.fixture
def sample_tree() -> TreeNode:
    """Returns a balanced binary tree for testing.

         1
        / \\
       2   3
      / \\ / \\
     4  5 6  7
    """
    return TreeNode.from_level_order([1, 2, 3, 4, 5, 6, 7])  # type: ignore[return-value]


@pytest.fixture
def skewed_tree() -> TreeNode:
    """Returns a left-skewed binary tree: 1 → 2 → 3 → 4."""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    return root


@pytest.fixture
def bst_tree() -> TreeNode:
    """Returns a valid BST.

         4
        / \\
       2   6
      / \\ / \\
     1  3 5  7
    """
    return TreeNode.from_level_order([4, 2, 6, 1, 3, 5, 7])  # type: ignore[return-value]


# ─── Linked List Fixtures ──────────────────────────────────────────────


@pytest.fixture
def sample_linked_list() -> ListNode:
    """Returns a linked list: 1 → 2 → 3 → 4 → 5."""
    return ListNode.from_list([1, 2, 3, 4, 5])  # type: ignore[return-value]


@pytest.fixture
def single_node_list() -> ListNode:
    """Returns a single-node linked list: 42."""
    return ListNode(42)


# ─── Array / Matrix Fixtures ──────────────────────────────────────────


@pytest.fixture
def sorted_array() -> list[int]:
    """Returns a sorted integer array."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def unsorted_array() -> list[int]:
    """Returns an unsorted integer array."""
    return [38, 27, 43, 3, 9, 82, 10]


@pytest.fixture
def sample_matrix() -> list[list[int]]:
    """Returns a 3×3 matrix for testing."""
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]


# ─── Graph Fixtures ───────────────────────────────────────────────────


@pytest.fixture
def adjacency_list_undirected() -> dict[int, list[int]]:
    """Returns an undirected graph as adjacency list.

    0 -- 1
    |    |
    2 -- 3
    """
    return {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2],
    }


@pytest.fixture
def adjacency_list_directed() -> list[list[int]]:
    """Returns a directed graph as adjacency list (5 vertices).

    0 → 1, 0 → 2
    1 → 3
    2 → 3
    3 → 4
    """
    return [
        [1, 2],  # 0
        [3],  # 1
        [3],  # 2
        [4],  # 3
        [],  # 4
    ]
