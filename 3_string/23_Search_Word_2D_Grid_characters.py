"""
Problem: Search Word in 2D Grid
Category: Strings
Pattern: 8-Directional Matrix Search

Time Complexity:  O(R * C * 8 * len(word)) - Checking 8 directions from each cell
Space Complexity: O(1) auxiliary space
"""


def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def search_from(x, y, n, m, word_len):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        nx, ny = x, y
        match = True
        for k in range(word_len):
            if not is_valid(nx, ny, n, m) or grid[nx][ny] != word[k]:
                match = False
                break
            nx += dx
            ny += dy
        if match:
            return True
    return False


class Solution:
    def searchWord(self, grid, word):
        n = len(grid)
        m = len(grid[0])
        word_len = len(word)
        result = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == word[0] and search_from(i, j, n, m, word_len):
                    result.append((i, j))
        result.sort()
        return result


if __name__ == "__main__":
    obj = Solution()
    grid = [
        ["a", "b", "c"],
        ["d", "r", "f"],
        ["g", "h", "i"],
    ]
    word = "abc"
    print(f"Occurrences of '{word}': {obj.searchWord(grid, word)}")
