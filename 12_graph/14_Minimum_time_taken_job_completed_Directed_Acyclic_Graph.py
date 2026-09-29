"""
Problem: Minimum Time Taken by Each Job in a DAG
Category: Graph Algorithms
Pattern: Topological Sort / Level-by-Level BFS

Time Complexity:  O(V + E) - Standard topological sort traversal
Space Complexity: O(V + E) - Graph representation and job times array
"""

from typing import List


class Solution:
    def minimumTime(self, n: int, m: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n + 1)]
        for i in range(m):
            adj[edges[i][0]].append(edges[i][1])
        indegree = [0] * (n + 1)
        for i in range(1, n + 1):
            for val in adj[i]:
                indegree[val] += 1
        q = []
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                ans[i] = 1
        while q:
            node = q.pop(0)
            for val in adj[node]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    q.append(val)
                    ans[val] = ans[node] + 1
        ans = ans[1:]
        return ans


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
    n, m = 10, 13
    edges = [
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 3],
        [2, 8],
        [2, 9],
        [3, 6],
        [4, 6],
        [4, 8],
        [5, 8],
        [6, 7],
        [7, 8],
        [8, 10],
    ]
    res = Solution().minimumTime(n, m, edges)
    print(f"Job completion times: {res}")
