# 📚 DSA Python Roadmap

This repository contains categorized solutions to Data Structures and Algorithms (DSA) problems using Python. Each topic below links to a detailed `README.md` file containing problem statements and solutions.

---

## 📌 Topic-wise Index

| No. | Topic                                                      | Description                                                           |
| --- | ---------------------------------------------------------- | --------------------------------------------------------------------- |
| 1   | [📦 Array](1_array/README.md)                              | Problems on arrays, subarrays, sliding window, etc.                   |
| 2   | [🧮 Matrix](2_matrix/README.md)                            | 2D arrays, traversal patterns, and pathfinding problems               |
| 3   | [🔤 String](3_string/README.md)                            | String manipulation, palindrome, hashing, and pattern matching        |
| 4   | [🔍 Search & Sort](4_search_sort/README.md)                | Sorting techniques, binary search, and efficient searching strategies |
| 5   | [🔗 Linked List](5_linklist/README.md)                     | Operations on singly, doubly, and circular linked lists               |
| 6   | [🌳 Binary Tree](6_binary_tree/README.md)                  | Tree traversals, structural views, and conversions                    |
| 7   | [🌲 Binary Search Tree](7_bst/README.md)                   | Insertion, deletion, LCA, and BST validation                          |
| 8   | [⚡ Greedy](8_greedy/README.md)                            | Optimization problems using greedy strategies                         |
| 9   | [🔁 Backtracking](9_backtracking/README.md)                | Constraint-based recursion and combinatorial problems                 |
| 10  | [🥞 Stack & Queue](10_stack_queues/README.md)              | Implementations and applications in parsing, sorting, and more        |
| 11  | [🛠️ Heap](11_heap/README.md)                               | Max-heap, min-heap, priority queues, and heap-based algorithms        |
| 12  | [🧭 Graph](12_graph/README.md)                             | Traversals, shortest paths, MST, and topological sort                 |
| 13  | [🌐 Trie](13_Trie/README.md)                               | Prefix trees for dictionary, autocomplete, and word search            |
| 14  | [📊 Dynamic Programming](14_dynamic_programming/README.md) | Memoization, tabulation, and optimal substructure problems            |
| 15  | [💡 Bit Manipulation](15_bit_manipulation/README.md)       | Bitwise tricks, binary representation problems                        |

---

## ⚙️ Setup & Development Guide

A step-by-step guide to set up and run this DSA project using [`uv`](https://astral.sh/uv/), a fast Python package manager.

### ✅ Requirements

- Python 3.12+
- [`uv`](https://astral.sh/uv/) (virtual environment and package management tool)

---

### 🚀 Getting Started

#### 1. Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a virtual environment

```bash
uv venv
```

3. Activate the virtual environment

```bash
source .venv/bin/activate
```

4. Install project dependencies

```bash
uv pip install -r requirements.txt
```

Alternatively:

```bash
uv sync
```

5. (Optional) Freeze current dependencies

```bash
uv pip freeze > requirements.txt
```

🔍 Code Quality & Pre-commit Hooks 10. Install pre-commit hooks

```bash
pre-commit install
```

11. Run pre-commit on all files

```bash
pre-commit run --all-files
```

########################################################
