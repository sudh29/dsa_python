"""
Problem: Dijkstra's Shortest Path Algorithm
Category: Graph Algorithms
Pattern: Greedy / Priority Queue (Min-Heap)

Time Complexity:  O((V + E) log V) using min-heap
Space Complexity: O(V + E) - Adjacency list and distance array
"""

import heapq


class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        # distances = [float('inf')] * V
        # distances[S] = 0
        # visited = set()
        # for _ in range(V):
        #     min_distance = float('inf')
        #     min_vertex = -1
        #     for v in range(V):
        #         if v not in visited and distances[v] < min_distance:
        #             min_distance = distances[v]
        #             min_vertex = v
        #     visited.add(min_vertex)
        #     for neighbor, weight in adj[min_vertex]:
        #         if neighbor not in visited:
        #             distances[neighbor] = min(distances[neighbor], distances[min_vertex] + weight)
        # return distances

        # One loop and min heap
        distances = [float("inf")] * V
        distances[S] = 0
        pq = [(0, S)]
        while pq:
            dist, vertex = heapq.heappop(pq)
            if dist > distances[vertex]:
                continue
            for neighbor, weight in adj[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))
        return distances


if __name__ == "__main__":
    v = 3
    adj = [[[1, 1], [2, 6]], [[0, 1], [2, 2]], [[1, 2], [0, 6]]]
    print(f"Shortest distances from 0: {Solution().dijkstra(v, adj, 0)}")
