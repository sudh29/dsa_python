"""
Problem: Find All Duplicate Subtrees Binary Tree
Category: Binary Trees
Pattern: Tree Traversal (DFS / BFS)

Time Complexity:  O(N) - Visits each node once
Space Complexity: O(H) - Recursion stack bounded by tree height
"""


class Solution:
    def printAllDups(self, root):
        subtree_map = {}
        res = []

        def dfs(node):
            if not node:
                return "null"
            s = ",".join([str(node.data), dfs(node.left), dfs(node.right)])

            if s in subtree_map:
                if subtree_map[s] == 1:
                    res.append(node)
                subtree_map[s] += 1
            else:
                subtree_map[s] = 1
            return s

        dfs(root)
        res = sorted(res, key=lambda x: x.data)
        return res
