"""
Problem: Check Graph Tree Or Not
Category: Binary Trees
Pattern: Tree Traversal (DFS / BFS)

Time Complexity:  O(N) - Visits each node once
Space Complexity: O(H) - Recursion stack bounded by tree height
"""


class Solution:
    def isTree(self, n, adj):
        visited = [False] * n
        if self.isCyclicUtil(0, visited, -1, adj):
            return 0
        # for i in range(n):
        #     if visited[i] == False:
        #         return 0
        # return 1
        return 1 if all(visited) else 0

    def isCyclicUtil(self, curr, visited, parent, adj):
        visited[curr] = True
        for i in adj[curr]:
            if not visited[i]:
                if self.isCyclicUtil(i, visited, curr, adj):
                    return True
            elif i != parent:
                return True
        return False
