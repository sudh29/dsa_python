"""
Problem: Graph Node
Category: Algorithms
Pattern: Algorithmic Pattern

Time Complexity:  O(N)
Space Complexity: O(1)
"""

from typing import Self


class GraphNode:
    """Standard graph node with integer value and neighbors list."""

    def __init__(self, val: int = 0, neighbors: list[Self] | None = None) -> None:
        self.val = val
        self.neighbors: list[Self] = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f"GraphNode({self.val})"


class DisjointSetUnion:
    """Disjoint Set Union (DSU) / Union-Find with path compression and rank."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True
