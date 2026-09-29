"""
Problem: Construct Binary Tree String Bracket Representation
Category: Binary Trees
Pattern: Tree Traversal (DFS / BFS)

Time Complexity:  O(N) - Visits each node once
Space Complexity: O(H) - Recursion stack bounded by tree height
"""


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def treeFromString(self, s: str) -> Node | None:
        def dfs(s):
            if not s:
                return None
            p = s.find("(")
            if p == -1:
                return Node(int(s))
            root = Node(int(s[:p]))
            start = p
            cnt = 0
            for i in range(p, len(s)):
                if s[i] == "(":
                    cnt += 1
                elif s[i] == ")":
                    cnt -= 1
                if cnt == 0:
                    if start == p:
                        root.left = dfs(s[start + 1 : i])
                        start = i + 1
                    else:
                        root.right = dfs(s[start + 1 : i])
            return root

        return dfs(s)
