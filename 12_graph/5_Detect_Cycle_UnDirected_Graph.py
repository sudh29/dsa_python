"""
Problem: Detect Cycle in an Undirected Graph
Category: Graph Algorithms
Pattern: BFS / DFS with Parent Tracking

Time Complexity:  O(V + E) - Traverses vertices and edges
Space Complexity: O(V) - Visited array and traversal queue/stack
"""

from typing import List


def dfs(val, graph, visited, parent):
    visited[val] = True
    for i in graph[val]:
        if not visited[i]:
            if dfs(i, graph, visited, val):
                return True
        elif i != parent:
            return True
    return False


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if dfs(i, adj, visited, -1):
                    return True
        return False


if __name__ == "__main__":
    v = 4
    adj = [[1, 2], [0, 2], [0, 1, 3], [2]]
    print(f"Cycle in undirected graph: {Solution().isCycle(v, adj)}")
