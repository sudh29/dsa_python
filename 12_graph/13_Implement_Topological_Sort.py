"""
Problem: Topological Sort (Kahn's Algorithm)
Category: Graph Algorithms
Pattern: In-Degree Array / BFS Queue (Kahn)

Time Complexity:  O(V + E) - Visits each vertex and decrements each edge once
Space Complexity: O(V) - In-degree array, queue, and result list
"""


class Solution:
    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # DFS
        # visited = [False] * V
        # stack = []

        # def dfs(node):
        #     visited[node] = True
        #     for neighbor in adj[node]:
        #         if not visited[neighbor]:
        #             dfs(neighbor)
        #     stack.append(node)

        # for i in range(V):
        #     if not visited[i]:
        #         dfs(i)
        # return stack[::-1]

        # BFS
        val = [0 for i in range(V)]
        res = []
        q = []
        for i in range(V):
            for j in adj[i]:
                val[j] += 1
        for i in range(V):
            if val[i] == 0:
                q.append(i)
        while len(q) != 0:
            data = q.pop(0)
            res.append(data)
            for j in adj[data]:
                val[j] -= 1
                if val[j] == 0:
                    q.append(j)
        return res


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == "__main__":
    n = 6
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    res = Solution().topoSort(n, adj)
    print(f"Topological order: {res}")
    assert check(adj, n, res)
