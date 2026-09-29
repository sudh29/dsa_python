"""
Problem: Breadth First Traversal of Graph
Category: Graph Algorithms
Pattern: Queue-based BFS Traversal

Time Complexity:  O(V + E) - Visits all vertices and edges
Space Complexity: O(V) - Visited array and BFS queue
"""

from typing import List


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        if V < 1:
            return
        visited = [False for _ in range(V)]
        res = []
        q = []
        q.append(0)
        visited[0] = True
        while q:
            value = q.pop(0)
            res.append(value)
            for i in adj[value]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        return res


if __name__ == "__main__":
    v = 5
    adj = [[1, 2, 3], [], [4], [], []]
    print(f"BFS traversal: {Solution().bfsOfGraph(v, adj)}")
