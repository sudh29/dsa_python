"""
Problem: Unique Paths in Grid with Obstacles (DP)
Category: Fundamentals / Dynamic Programming
Pattern: 2D Grid DP

Time Complexity:  O(m × n) - Fills each cell once
Space Complexity: O(m × n) - DP matrix (can be optimized to O(n))
"""


def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    """Counts the number of unique paths from top-left to bottom-right.

    Movement is restricted to right and down. Cells with value 1 are obstacles.

    Args:
        grid: m×n matrix where 0 = free, 1 = obstacle.

    Returns:
        Number of unique paths from (0,0) to (m-1, n-1).
    """
    if not grid or grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] if grid[i][0] == 0 else 0

    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] if grid[0][j] == 0 else 0

    # Fill rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    test_cases = [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 0], [0, 0]], 2),
        ([[1, 0], [0, 0]], 0),  # Start blocked
        ([[0, 0], [0, 1]], 0),  # End blocked
        ([[0]], 1),  # Single cell
    ]
    for grid, expected in test_cases:
        actual = unique_paths_with_obstacles(grid)
        assert actual == expected, f"Failed for {grid}: got {actual}, expected {expected}"
    print("All unique paths demonstrations passed!")
