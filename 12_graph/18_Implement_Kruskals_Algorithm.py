"""
Problem: Kruskal's Algorithm for Minimum Spanning Tree
Category: Graph Algorithms
Pattern: Greedy / Disjoint Set Union (Union-Find)

Time Complexity:  O(E log E) - Dominated by sorting edge list
Space Complexity: O(V + E) - DSU structures and edge list
"""

from heapq import heappop, heappush


class Solution:
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        pq = []
        in_mst = [False] * V
        heappush(pq, (0, 0))
        mst_weight = 0
        while pq:
            weight, u = heappop(pq)
            if in_mst[u]:
                continue
            in_mst[u] = True
            mst_weight += weight
            for neighbor, wt in adj[u]:
                if not in_mst[neighbor]:
                    heappush(pq, (wt, neighbor))
        return mst_weight


if __name__ == "__main__":
    v = 3
    adj = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[0, 1], [1, 3]]]
    print(f"MST total weight: {Solution().spanningTree(v, adj)}")
