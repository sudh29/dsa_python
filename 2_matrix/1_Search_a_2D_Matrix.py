"""
Problem: Search A 2D Matrix
Category: Matrix
Pattern: Binary Search / Staircase Search (Top-Right to Bottom-Left)

Time Complexity:  O(R + C) or O(log(R * C))
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j >= 0:
            print(i, j)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
