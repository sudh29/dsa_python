class Solution:
    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        if root is None:
            return
        min_hd = 0
        max_hd = 0
        q = [(root, 0)]
        m = dict()
        while q:
            curr, hd = q.pop(0)
            if hd not in m.keys():
                m[hd] = curr.data
            if curr.left is not None:
                q.append((curr.left, hd - 1))
                min_hd = min(min_hd, hd - 1)
            if curr.right is not None:
                q.append((curr.right, hd + 1))
                max_hd = max(max_hd, hd + 1)
        res = []
        for i in range(min_hd, max_hd + 1):
            res.append(m[i])
        return res
