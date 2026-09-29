"""
Problem: Iterative DFS and BFS using Stack and Queue
Category: Graph Algorithms
Pattern: Graph Traversal (Iterative)

Time Complexity:  O(V + E) - Each vertex and edge visited once in adjacency list representation
Space Complexity: O(V) - Visited set and traversal data structure (stack/queue)
"""

from collections import deque


def bfs_iterative(graph: dict[str, set[str]], start: str) -> list[str]:
    """Performs iterative BFS using a queue.

    Args:
        graph: Adjacency list representation using sets.
        start: Starting vertex.

    Returns:
        List of vertices in BFS traversal order.
    """
    visited: set[str] = {start}
    queue: deque[str] = deque([start])
    path: list[str] = []

    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for neighbor in sorted(graph.get(vertex, set())):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return path


def dfs_iterative(graph: dict[str, set[str]], start: str) -> list[str]:
    """Performs iterative DFS using a stack.

    Args:
        graph: Adjacency list representation using sets.
        start: Starting vertex.

    Returns:
        List of vertices in DFS traversal order.
    """
    visited: set[str] = {start}
    stack: list[str] = [start]
    path: list[str] = []

    while stack:
        vertex = stack.pop()
        path.append(vertex)
        for neighbor in sorted(graph.get(vertex, set())):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return path


if __name__ == "__main__":
    graph: dict[str, set[str]] = {
        "0": {"1", "2"},
        "1": {"0", "3", "4"},
        "2": {"0", "4"},
        "3": {"1", "4"},
        "4": {"1", "2", "3"},
    }

    bfs_result = bfs_iterative(graph, "0")
    assert bfs_result[0] == "0", f"BFS should start at '0', got {bfs_result[0]}"
    assert set(bfs_result) == {"0", "1", "2", "3", "4"}, "BFS should visit all vertices"

    dfs_result = dfs_iterative(graph, "0")
    assert dfs_result[0] == "0", f"DFS should start at '0', got {dfs_result[0]}"
    assert set(dfs_result) == {"0", "1", "2", "3", "4"}, "DFS should visit all vertices"

    print("All iterative DFS/BFS demonstrations passed!")
