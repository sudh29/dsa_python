"""
Problem: Depth First Traversal of Graph
Category: Graph Algorithms
Pattern: Recursive / Stack-based DFS

Time Complexity:  O(V + E) - Visits all reachable vertices and traverses each edge
Space Complexity: O(V) - Recursion call stack and visited array
"""


def solve_dfs(val, visited, graph, ans):
    visited[val] = True
    ans.append(val)
    for i in graph[val]:
        if not visited[i]:
            solve_dfs(i, visited, graph, ans)


class Solution:
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # print(adj)
        if V < 1:
            return
        visited = [False for _ in range(V)]
        res = []
        solve_dfs(0, visited, adj, res)  # recursion stack
        return res

        # Normal stack
        # if V < 1:
        #     return []
        # visited = [False] * V
        # res = []
        # stack = []
        # stack.append(0)
        # visited[0] = True
        # while stack:
        #     value = stack.pop()
        #     res.append(value)
        #     for i in reversed(adj[value]):
        #         if not visited[i]:
        #             stack.append(i)
        #             visited[i] = True
        # return res


if __name__ == "__main__":
    v = 5
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(f"DFS traversal: {Solution().dfsOfGraph(v, adj)}")
