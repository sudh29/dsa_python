"""
Problem: Maximum Size Square Sub-Matrix with All 1s
Category: Dynamic Programming
Pattern: 2D Grid DP / Min of Three Neighbors

Time Complexity:  O(R * C) - Single pass through matrix
Space Complexity: O(R * C) - DP table storage
"""

from typing import List


class Solution:
    def maxSquare(self, n: int, m: int, mat: List[List[int]]) -> int:
        dp = [[0] * m for _ in range(n)]
        max_side = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side


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
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    print(f"Max square size: {Solution().maxSquare(len(mat), len(mat[0]), mat)}")
