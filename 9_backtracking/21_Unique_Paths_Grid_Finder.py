"""
Problem: Unique Paths in a Grid (Path Finder)
Category: Backtracking
Pattern: Grid Backtracking (Right and Down moves)

Time Complexity:  O(2^(m+n)) - Explores all possible paths via recursion
Space Complexity: O(m+n) - Maximum recursion depth is path length
"""


def find_path(
    matrix: list[list[int]], pos: tuple[int, int], n: int
) -> list[tuple[int, int]] | None:
    """Finds a path from pos to (n-1, n-1) in the grid using backtracking.

    Only moves right or down through cells with value 1.

    Args:
        matrix: n×n grid where 1 = passable, 0 = blocked.
        pos: Current position as (row, col).
        n: Size of the grid.

    Returns:
        List of (row, col) coordinates forming the path, or None if no path exists.
    """
    x, y = pos

    if x == n - 1 and y == n - 1:
        return [(x, y)]

    # Try moving down
    if x + 1 < n and matrix[x + 1][y] == 1:
        result = find_path(matrix, (x + 1, y), n)
        if result is not None:
            return [(x, y)] + result

    # Try moving right
    if y + 1 < n and matrix[x][y + 1] == 1:
        result = find_path(matrix, (x, y + 1), n)
        if result is not None:
            return [(x, y)] + result

    return None


if __name__ == "__main__":
    matrix = [
        [1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    path = find_path(matrix, (0, 0), 5)
    assert path is not None, "Path should exist"
    assert path[0] == (0, 0), "Path should start at (0,0)"
    assert path[-1] == (4, 4), "Path should end at (4,4)"

    # Blocked grid: no path
    blocked = [
        [1, 0],
        [0, 1],
    ]
    assert find_path(blocked, (0, 0), 2) is None

    # Trivial 1×1 grid
    assert find_path([[1]], (0, 0), 1) == [(0, 0)]

    print("All path finder demonstrations passed!")
