"""
Problem: Detect Cycle in a Directed Graph
Category: Graph Algorithms
Pattern: DFS with Recursion Stack / Color Marking

Time Complexity:  O(V + E) - Standard DFS cycle detection
Space Complexity: O(V) - Visited and recursion stack arrays
"""


def dfs(val, graph, visited, rec_stack):
    visited[val] = True
    rec_stack[val] = True
    for i in graph[val]:
        if not visited[i]:
            if dfs(i, graph, visited, rec_stack):
                return True
        elif rec_stack[i]:
            return True
    rec_stack[val] = False
    return False


class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: list[list[int]]) -> bool:
        visited = [False] * V
        rec_stack = [False] * V
        for i in range(V):
            if not visited[i]:
                if dfs(i, adj, visited, rec_stack):
                    return True
        return False


if __name__ == "__main__":
    v = 4
    adj = [[1], [2], [3], [1]]
    print(f"Cycle detected: {Solution().isCyclic(v, adj)}")
