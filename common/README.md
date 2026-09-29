# 🧱 Common Abstractions & Data Structures

Centralized, fully typed, reusable data structures and algorithms shared across the repository and test harnesses.

---

## 📌 Available Data Structures

### 1. Linked Lists (`common.list_node`)
- [`ListNode`](list_node.py): Singly linked list node with `from_list()`, `to_list()`, structural `__eq__`, `__repr__`, and loop detection.
- [`DoublyListNode`](list_node.py): Doubly linked list node with bidirectional pointer support (`prev`, `next`).

```python
from common.list_node import ListNode

head = ListNode.from_list([1, 2, 3, 4, 5])
assert head.to_list() == [1, 2, 3, 4, 5]
```

### 2. Binary Trees (`common.tree_node`)
- [`TreeNode`](tree_node.py): Binary tree node with level-order serialization (`to_level_order()`), deserialization from lists with `None` (`from_level_order()`), and structural equality.

```python
from common.tree_node import TreeNode

root = TreeNode.from_level_order([1, 2, 3, None, 4, 5, None])
assert root.to_level_order() == [1, 2, 3, None, 4, 5, None]
```

### 3. Graphs & Disjoint Sets (`common.graph_node`)
- [`GraphNode`](graph_node.py): Adjacency list graph node with typed neighbor collections.
- [`DisjointSetUnion`](graph_node.py): Production-ready Disjoint Set Union (DSU / Union-Find) featuring path compression and union by rank.

```python
from common.graph_node import DisjointSetUnion

dsu = DisjointSetUnion(5)
dsu.union(0, 1)
dsu.union(1, 2)
assert dsu.connected(0, 2) is True
```

### 4. Prefix Trees (`common.trie_node`)
- [`TrieNode`](trie_node.py): Prefix trie node supporting both fixed-alphabet indexing and dictionary branches.

---

## 🧪 Testing

The entire common suite is rigorously verified by [`tests/test_common.py`](../tests/test_common.py):

```bash
uv run pytest tests/test_common.py -v
```
