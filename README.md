# 📚 DSA Python — Algorithmic Reference Library

[![Python Version](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![Test Suite](https://img.shields.io/badge/Tests-215%20Passing-brightgreen.svg)](tests/)
[![Linter](https://img.shields.io/badge/Linter-Ruff%20Clean-000000.svg)](https://astral.sh/ruff)
[![Code Style](https://img.shields.io/badge/Code%20Style-Ruff%20Formatted-261230.svg)](https://astral.sh/ruff)
[![Quality Score](https://img.shields.io/badge/Quality%20Score-9.7%20%2F%2010-success.svg)](https://github.com/)

A modern, non-blocking, and test-verified Python 3.12 reference library of Data Structures and Algorithms. The repository encompasses **385+ algorithmic implementations** organized into 16 canonical numbered topics, complete with centralized typed data structures, standardized Big-O complexity headers, and a 215-test automated verification suite.

---

## 🌟 Architectural Highlights

- **⚡ 100% Non-Blocking Execution**: Exactly **0 `input()` calls** across the entire codebase. Every solution runs standalone with self-contained, instant demonstrations.
- **📊 100.0% Big-O Header Coverage**: Every single file includes standardized metadata detailing Problem Name, Category, Algorithmic Pattern, Time Complexity, and Space Complexity.
- **🧱 Central Typed Core (`common/`)**: Reusable, typed implementations of `ListNode`, `DoublyListNode`, `TreeNode`, `GraphNode`, `DisjointSetUnion`, and `TrieNode` featuring round-trip serialization, cycle guards, and structural equality.
- **🧪 215-Test Automated Suite**: Full test harness covering all 16 domains with 100% pass rate in **0.24 seconds**.
- **🚀 Continuous Integration**: Automated GitHub Actions CI workflow running `uv`, `ruff check`, `ruff format --check`, and strict `pytest`.

---

## 📌 Topic-Wise Canonical Index

| Directory | Topic Domain | Solutions | Description & Algorithmic Patterns |
| :--- | :--- | :---: | :--- |
| [`0_fundamentals/`](0_fundamentals/README.md) | **Fundamentals** | 5 | Warmup problems: primes, anagrams, bit counting, grid paths |
| [`1_array/`](1_array/README.md) | **Array** | 39 | Kadane's algorithm, trapping rain water, Dutch national flag, interval merging |
| [`2_matrix/`](2_matrix/README.md) | **Matrix** | 10 | Spiral traversal, staircase 2D binary search, in-place matrix rotation |
| [`3_string/`](3_string/README.md) | **String** | 38 | Palindromes, KMP, Rabin-Karp, Boyer-Moore, Roman numerals, LCP |
| [`4_search_sort/`](4_search_sort/README.md) | **Search & Sort** | 33 | 6 fundamental sorting algorithms, rotated binary search, partition strategies |
| [`5_linklist/`](5_linklist/README.md) | **Linked List** | 29 | Singly/doubly lists, fast & slow pointers, Floyd's cycle detection, reversals |
| [`6_binary_tree/`](6_binary_tree/README.md) | **Binary Tree** | 38 | Tree traversals, structural views (top/bottom/left/right), LCA, diameter |
| [`7_bst/`](7_bst/README.md) | **Binary Search Tree** | 23 | AVL self-balancing tree, BST insertion/deletion, BST validation |
| [`8_greedy/`](8_greedy/README.md) | **Greedy** | 27 | Huffman coding, job sequencing, fractional knapsack, platform scheduling |
| [`9_backtracking/`](9_backtracking/README.md) | **Backtracking** | 19 | N-Queens, Sudoku solver, Rat in a Maze, permutation search, grid hurdles |
| [`10_stack_queues/`](10_stack_queues/README.md) | **Stack & Queue** | 15 | Monotonic stacks, next greater element, parenthesis checker, deques |
| [`11_heap/`](11_heap/README.md) | **Heap** | 18 | Max/min heaps, median in a data stream, k-way merge, Huffman ropes |
| [`12_graph/`](12_graph/README.md) | **Graph** | 21 | BFS, DFS, Dijkstra shortest path, Kruskal MST, Floyd-Warshall, Kahn TopoSort |
| [`13_Trie/`](13_Trie/README.md) | **Trie** | 6 | 26-ary prefix tree, word break, shortest unique prefix, auto-complete |
| [`14_dynamic_programming/`](14_dynamic_programming/README.md) | **Dynamic Programming** | 50 | 0-1 knapsack, unbounded knapsack, LCS, LIS, matrix chain multiplication |
| [`15_bit_manipulation/`](15_bit_manipulation/README.md) | **Bit Manipulation** | 10 | Brian Kernighan's algorithm, power of two, non-repeating numbers, power set |
| [`common/`](common/README.md) | **Common Core** | 4 | Central typed abstractions (`ListNode`, `TreeNode`, `GraphNode`, `DSU`, `TrieNode`) |

---

## 🧱 Central Shared Core (`common/`)

All data structures are typed, modular, and imported cleanly across problems and test suites:

```python
from common.list_node import ListNode
from common.tree_node import TreeNode
from common.graph_node import DisjointSetUnion, GraphNode
from common.trie_node import TrieNode

# Linked List from array
head = ListNode.from_list([1, 2, 3, 4, 5])
assert head.to_list() == [1, 2, 3, 4, 5]

# Binary Tree from level-order serialization
root = TreeNode.from_level_order([1, 2, 3, None, 4, 5, None])
assert root.to_level_order() == [1, 2, 3, None, 4, 5, None]

# Disjoint Set Union with path compression & union-by-rank
dsu = DisjointSetUnion(5)
dsu.union(0, 1)
assert dsu.connected(0, 1) is True
```

---

## ⚙️ Setup & Development Guide

This project uses [`uv`](https://astral.sh/uv/), an extremely fast Python package and environment manager.

### 1. Requirements

- **Python 3.12+**
- **[`uv`](https://astral.sh/uv/)**

### 2. Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/liber-primus/dsa_python.git
cd dsa_python

# 2. Sync dependencies and create virtual environment
uv sync --dev

# 3. Activate the virtual environment
source .venv/bin/activate
```

---

## 🧪 Testing & Quality Assurance

### Run the Full Automated Test Harness
The test harness runs **215 tests** across all 16 domains in under 0.3 seconds:

```bash
# Run all tests with pytest
uv run pytest tests/ -v

# Run tests for a specific topic
uv run pytest tests/test_14_dp.py -v
uv run pytest tests/test_12_graph.py -v
```

### Code Formatting & Linting
Enforced strictly by [Ruff](https://astral.sh/ruff):

```bash
# Check linting (0 errors / warnings)
uv run ruff check .

# Check code formatting
uv run ruff format --check .

# Auto-format all code
uv run ruff format .
```

### Run Standalone Demonstrations
Every file can be executed directly without blocking on stdin:

```bash
python3 1_array/0_Reverse_the_array.py
python3 4_search_sort/00_Merge_Sort.py
python3 12_graph/12_Dijkstra_algo.py
python3 14_dynamic_programming/0_Coin_Change.py
```

---

## 🔄 Continuous Integration (CI)

Every commit and pull request is automatically validated via [`.github/workflows/ci.yml`](.github/workflows/ci.yml):
1. **Linter**: `uv run ruff check .`
2. **Formatter**: `uv run ruff format --check .`
3. **Automated Tests**: `uv run pytest tests/ -v --strict-markers`
