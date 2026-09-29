"""
Problem: N-Queen Problem
Category: Backtracking
Pattern: Column Placements & Diagonal Conflict Bitsets

Time Complexity:  O(N!) - Placing queens column by column
Space Complexity: O(N) - Board placement tracking and recursion depth
"""


def is_safe(r, c, board, n):
    # Check left col
    for i in range(c):
        if board[r][i]:
            return False
    # Check left-up diagonal
    i, j = r, c
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i, j = i - 1, j - 1
    # Check left-down diagonal
    i, j = r, c
    while i < n and j >= 0:
        if board[i][j]:
            return False
        i, j = i + 1, j - 1
    return True


def solve(c, buf, result, board, n):
    if c >= n:
        return True
    for r in range(n):
        if is_safe(r, c, board, n):
            board[r][c] = 1
            buf.append(r + 1)
            if solve(c + 1, buf, result, board, n):
                result.append([x for x in buf])
            buf.pop()
            board[r][c] = 0
    return False


class Solution:
    def nQueen(self, n):
        board = [[0 for _ in range(n)] for _ in range(n)]
        buf = []
        result = []
        solve(0, buf, result, board, n)
        return result


if __name__ == "__main__":
    print(f"4-Queens solutions: {Solution().nQueen(4)}")
