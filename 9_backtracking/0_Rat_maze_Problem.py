"""
Problem: Rat in a Maze Problem
Category: Backtracking
Pattern: DFS with Backtracking / Lexicographical Paths

Time Complexity:  O(4^(N^2)) worst case path enumeration
Space Complexity: O(N^2) - Visited matrix and recursion stack
"""


def dfs(i, j, s, matrix, n, visited_mat, ans):
    if i < 0 or j < 0 or i >= n or j >= n:
        return
    if matrix[i][j] == 0 or visited_mat[i][j] == 1:
        return
    if i == n - 1 and j == n - 1:
        ans.append(s)
        return
    visited_mat[i][j] = 1

    dfs(i - 1, j, s + "U", matrix, n, visited_mat, ans)  # Up
    dfs(i + 1, j, s + "D", matrix, n, visited_mat, ans)  # Down
    dfs(i, j - 1, s + "L", matrix, n, visited_mat, ans)  # Left
    dfs(i, j + 1, s + "R", matrix, n, visited_mat, ans)  # Right

    visited_mat[i][j] = 0  # Backtrack


class Solution:
    def findPath(self, m, n):
        visited = [[0 for _ in range(n)] for _ in range(n)]
        ans = []
        string = ""
        dfs(0, 0, string, m, n, visited, ans)
        ans.sort()
        return ans if ans else ["-1"]


if __name__ == "__main__":
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    print(f"Paths in maze: {Solution().findPath(maze, 4)}")
