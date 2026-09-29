"""
Problem: Create and Print Adjacency List Graph
Category: Graph Algorithms
Pattern: Adjacency List Construction

Time Complexity:  O(V + E) - Linear in vertices and edges
Space Complexity: O(V + E) - Storage for adjacency lists
"""

from typing import List


class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(V)]
        for edge in edges:
            u, v = edge
            res[u].append(v)
            res[v].append(u)
        return res


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        return []

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        return []

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    v = 4
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    print(f"Adjacency list: {Solution().printGraph(v, edges)}")
