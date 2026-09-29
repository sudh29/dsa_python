"""
Problem: Clone A Graph
Category: Graph Algorithms
Pattern: Breadth-First Search / Depth-First Search

Time Complexity:  O(V + E)
Space Complexity: O(V) - Visited set and traversal queue/stack
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node:
            return None
        visited = {}
        queue = [node]
        cloned_node = Node(node.val)
        visited[node] = cloned_node
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    cloned_neighbor = Node(neighbor.val)
                    visited[neighbor] = cloned_neighbor
                    visited[current].neighbors.append(cloned_neighbor)
                    queue.append(neighbor)
                else:
                    visited[current].neighbors.append(visited[neighbor])
        return visited[node]
