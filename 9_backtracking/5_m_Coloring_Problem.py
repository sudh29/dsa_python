"""
Problem: M-Coloring Problem
Category: Backtracking
Pattern: Vertex Coloring with Conflict Checking

Time Complexity:  O(M^V) worst case exponential exploration
Space Complexity: O(V) - Color assignment array
"""


def valid(node, graph, color, c, graph_len):
    for i in range(graph_len):
        if graph[node][i] and color[i] == c:
            return False
    return True


def solve(node, m, color, graph, graph_len):
    if node == graph_len:
        return True
    for c in range(1, m + 1):
        if valid(node, graph, color, c, graph_len):
            color[node] = c
            if solve(node + 1, m, color, graph, graph_len):
                return True
            color[node] = 0
    return False


# Function to determine if graph can be coloured with at most M colours such
# that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    color = [0] * V
    if solve(0, k, color, graph, V):
        return 1
    return 0


if __name__ == "__main__":
    graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    print(f"3-clique with 3 colors: {graphColoring(graph, 3, 3)}")
