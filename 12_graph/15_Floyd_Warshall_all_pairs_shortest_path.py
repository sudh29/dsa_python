"""
Problem: Floyd-Warshall All-Pairs Shortest Path
Category: Graph Algorithms
Pattern: Dynamic Programming on Graphs

Time Complexity:  O(V^3) - Triple nested loop over all vertices
Space Complexity: O(V^2) - Distance matrix for all vertex pairs
"""

INF = float("inf")


def floyd_warshall(num_vertices: int, edges: list[tuple[int, int, int]]) -> list[list[float]]:
    """Computes shortest distances between every pair of vertices.

    Args:
        num_vertices: Number of vertices (0-indexed).
        edges: List of (source, destination, weight) tuples.

    Returns:
        2D distance matrix where dist[i][j] is the shortest distance from i to j.
    """
    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    # Test case: 4 vertices with known shortest paths
    edges = [(0, 1, 5), (0, 3, 10), (1, 2, 3), (2, 3, 1)]
    result = floyd_warshall(4, edges)

    assert result[0][0] == 0
    assert result[0][1] == 5
    assert result[0][2] == 8  # 0→1→2
    assert result[0][3] == 9  # 0→1→2→3
    assert result[1][2] == 3
    assert result[2][3] == 1

    # Test disconnected vertices
    assert result[1][0] == INF
    assert result[3][0] == INF

    print("All Floyd-Warshall demonstrations passed!")
