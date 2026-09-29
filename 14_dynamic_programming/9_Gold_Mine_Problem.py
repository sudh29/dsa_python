"""
Problem: Gold Mine Problem
Category: Dynamic Programming
Pattern: 2D Grid DP / Column-by-Column Transitions

Time Complexity:  O(N * M) - Visiting each cell of N x M gold mine
Space Complexity: O(N * M) - DP matrix storage
"""


class Solution:
    def maxGold(self, n, m, M):
        for col in range(m - 2, -1, -1):
            for row in range(n):
                right = M[row][col + 1]
                right_up = M[row - 1][col + 1] if row > 0 else 0
                right_down = M[row + 1][col + 1] if row < n - 1 else 0
                M[row][col] += max(right, right_up, right_down)
        return max(M[row][0] for row in range(n))


if __name__ == "__main__":
    mine = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
    print(f"Max gold collected: {Solution().maxGold(len(mine), len(mine[0]), mine)}")
