"""
Problem: BFS on Adjacency Matrix Graph
Category: Graph Algorithms
Pattern: Breadth-First Search (Level-Order Traversal)

Time Complexity:  O(V^2) - Checking all columns for each dequeued vertex in adjacency matrix
Space Complexity: O(V) - Visited array and BFS queue
"""

from collections import deque


class AdjacencyMatrixGraph:
    """Graph representation using an adjacency matrix."""

    def __init__(self, size: int) -> None:
        self.size = size
        self.matrix: list[list[int]] = [[0] * size for _ in range(size)]

    def add_edge(self, u: int, v: int) -> None:
        """Adds a directed edge from vertex u to vertex v."""
        self.matrix[u][v] = 1

    def bfs(self, source: int) -> list[int]:
        """Performs BFS traversal starting from the source vertex.

        Returns:
            List of vertices in BFS traversal order.
        """
        visited = [False] * self.size
        visited[source] = True
        queue: deque[int] = deque([source])
        path: list[int] = []

        while queue:
            vertex = queue.popleft()
            path.append(vertex)
            for i in range(self.size):
                if not visited[i] and self.matrix[vertex][i] == 1:
                    visited[i] = True
                    queue.append(i)

        return path


if __name__ == "__main__":
    g = AdjacencyMatrixGraph(8)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 6)
    g.add_edge(2, 7)
    g.add_edge(3, 7)

    result = g.bfs(0)
    assert result == [0, 1, 2, 3, 4, 5, 6, 7], f"BFS failed: got {result}"

    # Single vertex graph
    g2 = AdjacencyMatrixGraph(1)
    assert g2.bfs(0) == [0]

    print("All BFS adjacency matrix demonstrations passed!")
