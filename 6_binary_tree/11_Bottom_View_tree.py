"""
Problem: Bottom View Tree
Category: Binary Trees
Pattern: Tree Traversal (DFS / BFS)

Time Complexity:  O(N) - Visits each node once
Space Complexity: O(H) - Recursion stack bounded by tree height
"""


class Solution:
    def bottomView(self, root):
        if root is None:
            return []
        min_hd = 0
        max_hd = 0
        q = [(root, 0)]
        m = dict()
        while q:
            curr, hd = q.pop(0)
            m[hd] = curr.data
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            if curr.left:
                q.append((curr.left, hd - 1))
            if curr.right:
                q.append((curr.right, hd + 1))

        res = []
        for i in range(min_hd, max_hd + 1):
            res.append(m[i])
        return res
