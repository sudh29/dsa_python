"""
Problem: Graph Representation using Adjacency Dictionary
Category: Graph Algorithms
Pattern: Graph Construction & Representation

Time Complexity:  O(1) per edge addition; O(V + E) for full traversal
Space Complexity: O(V + E) - Adjacency list storage
"""

from collections import defaultdict


class AdjacencyDictGraph:
    """Directed graph using a dictionary-based adjacency list representation."""

    def __init__(self) -> None:
        self.graph: dict[int, list[int]] = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        """Adds a directed edge from vertex u to vertex v."""
        self.graph[u].append(v)

    def get_neighbors(self, u: int) -> list[int]:
        """Returns the list of neighbors for vertex u."""
        return self.graph[u]

    def vertices(self) -> set[int]:
        """Returns all vertices that appear in the graph."""
        all_v: set[int] = set()
        for u in self.graph:
            all_v.add(u)
            for v in self.graph[u]:
                all_v.add(v)
        return all_v


if __name__ == "__main__":
    g = AdjacencyDictGraph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    assert g.get_neighbors(0) == [1, 2]
    assert g.get_neighbors(2) == [0, 3]
    assert g.get_neighbors(3) == [3]
    assert g.vertices() == {0, 1, 2, 3}

    print("All adjacency dict graph demonstrations passed!")
