"""
Problem: Sudoku Solver
Category: Backtracking
Pattern: Constraint Satisfaction / Backtracking Search

Time Complexity:  O(9^(empty_cells)) worst case with early pruning
Space Complexity: O(81) - Fixed 9x9 grid recursion stack
"""


def find_next_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None, None


def is_valid(grid, guess, row, col):
    row_vals = grid[row]
    if guess in row_vals:
        return False
    col_vals = [grid[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_st = (row // 3) * 3
    col_st = (col // 3) * 3
    for r in range(row_st, row_st + 3):
        for c in range(col_st, col_st + 3):
            if grid[r][c] == guess:
                return False
    return True


class Solution:
    def SolveSudoku(self, grid):
        row, col = find_next_empty(grid)
        if row is None:
            return True
        if grid[row][col] == 0:
            for guess in range(1, 10):
                if is_valid(grid, guess, row, col):
                    grid[row][col] = guess
                    if self.SolveSudoku(grid):
                        return True
                    grid[row][col] = 0
            return False
        return True

    def printGrid(self, arr):
        for row in range(9):
            for col in range(9):
                print(arr[row][col], end=" ")


if __name__ == "__main__":
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]
    sol = Solution()
    if sol.SolveSudoku(grid):
        print("Sudoku solved successfully.")
