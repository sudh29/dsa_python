"""
Problem: Rat in a Maze Problem
Category: Graph Algorithms
Pattern: Backtracking / 4-Directional DFS

Time Complexity:  O(4^(N^2)) worst case exhaustive path search
Space Complexity: O(N^2) - Recursion call stack and visited matrix
"""


def dfs(m, n, paths, curr_path, i, j, visited):
    if i < 0 or j < 0 or i >= n or j >= n:
        return
    if m[i][j] == 0 or visited[i][j] == 1:
        return

    if i == n - 1 and j == n - 1:
        paths.append(curr_path)
        return

    visited[i][j] = 1
    dfs(m, n, paths, curr_path + "U", i - 1, j, visited)
    dfs(m, n, paths, curr_path + "D", i + 1, j, visited)
    dfs(m, n, paths, curr_path + "L", i, j - 1, visited)
    dfs(m, n, paths, curr_path + "R", i, j + 1, visited)
    visited[i][j] = 0


class Solution:
    def findPath(self, m, n):
        res = []
        if m[0][0] == 0 or m[n - 1][n - 1] == 0:
            return res
        visited = [[0] * n for _ in range(n)]
        dfs(m, n, res, "", 0, 0, visited)
        res.sort()
        return res


if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1],
    ]
    print(f"Paths in maze: {Solution().findPath(maze, 4)}")
