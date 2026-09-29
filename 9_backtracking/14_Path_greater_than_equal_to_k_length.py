"""
Problem: Path of Greater Than Equal to K Length
Category: Backtracking
Pattern: DFS with Backtracking & Visited Set

Time Complexity:  O(V!) worst case simple path enumeration
Space Complexity: O(V) - Visited array and recursion depth
"""


def dfs(val, visited, graph, path_len, K):
    if path_len >= K:
        return 1
    visited.add(val)
    for n, w in graph[val]:
        if n not in visited:
            if dfs(n, visited, graph, path_len + w, K):
                return 1
    visited.remove(val)
    return 0


class Solution:
    def pathMoreThanK(self, V, E, K, A):
        graph = [[] for _ in range(V)]
        for i in range(0, len(A), 3):
            src, dest, weight = A[i], A[i + 1], A[i + 2]
            graph[src].append((dest, weight))
            graph[dest].append((src, weight))
        # print(graph)

        visited = set()
        return dfs(0, visited, graph, 0, K)


if __name__ == "__main__":
    edges = [0, 1, 4, 0, 7, 8, 1, 2, 8, 1, 7, 11, 2, 3, 7, 2, 5, 4, 3, 4, 9, 3, 5, 14]
    print(f"Path >= 58 exists: {Solution().pathMoreThanK(9, 8, 58, edges)}")
