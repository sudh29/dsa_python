"""
Problem: Find the Number of Islands (8 directions)
Category: Graph Algorithms
Pattern: Connected Components / BFS / DFS Grid Traversal

Time Complexity:  O(R * C) - Each cell is visited constant times
Space Complexity: O(R * C) - Visited array and queue
"""

import sys

sys.setrecursionlimit(10**8)


def dfs(row, col, grid):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
        return
    grid[row][col] = -1

    dfs(row + 1, col, grid)
    dfs(row - 1, col, grid)
    dfs(row, col + 1, grid)
    dfs(row, col - 1, grid)
    dfs(row + 1, col + 1, grid)
    dfs(row + 1, col - 1, grid)
    dfs(row - 1, col + 1, grid)
    dfs(row - 1, col - 1, grid)


class Solution:
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        num_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j, grid)
                    num_islands += 1
        return num_islands


if __name__ == "__main__":
    grid = [
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 0],
    ]
    print(f"Number of islands: {Solution().numIslands(grid)}")
