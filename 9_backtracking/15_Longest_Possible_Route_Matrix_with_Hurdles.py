"""
Problem: Longest Possible Route in a Matrix with Hurdles
Category: Backtracking
Pattern: Exhaustive DFS Backtracking

Time Complexity:  O(4^(R*C)) worst case path exploration
Space Complexity: O(R * C) - Visited array and recursion stack
"""

from typing import List


def solve(mat, n, m, i, j, x, y, visited, curr, ans):
    if i == x and j == y:
        ans[0] = max(ans[0], curr)
        return
    if i < 0 or j < 0 or i >= n or j >= m or mat[i][j] == 0 or visited[i][j]:
        return

    visited[i][j] = True
    if j != m - 1 and mat[i][j + 1] > 0:
        solve(mat, n, m, i, j + 1, x, y, visited, curr + 1, ans)
    if i != n - 1 and mat[i + 1][j] > 0:
        solve(mat, n, m, i + 1, j, x, y, visited, curr + 1, ans)
    if j != 0 and mat[i][j - 1] > 0:
        solve(mat, n, m, i, j - 1, x, y, visited, curr + 1, ans)
    if i != 0 and mat[i - 1][j] > 0:
        solve(mat, n, m, i - 1, j, x, y, visited, curr + 1, ans)
    visited[i][j] = False


class Solution:
    def longestPath(
        self, mat: List[List[int]], n: int, m: int, xs: int, ys: int, xd: int, yd: int
    ) -> int:
        if xs < 0 or xs >= n or ys < 0 or ys >= m or xd < 0 or xd >= n or yd < 0 or yd >= m:
            return -1

        visited = [[False for _ in range(m)] for _ in range(n)]
        ans = [-1]
        solve(mat, n, m, xs, ys, xd, yd, visited, 0, ans)
        return ans[0]


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, *args):
        return []

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, *args):
        return []

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    mat = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ]
    print(f"Longest route from (0,0) to (1,3): {Solution().longestPath(mat, 3, 4, 0, 0, 1, 3)}")
