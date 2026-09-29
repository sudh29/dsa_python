"""
Problem: Maximum Size Rectangle in Binary Matrix
Category: Matrix
Pattern: Monotonic Stack / Largest Rectangle in Histogram

Time Complexity:  O(R * C) - Each cell is processed into histogram and pushed/popped from stack once per row
Space Complexity: O(C) - Histogram array and stack for current row
"""


def max_histogram_area(hist):
    stack = []
    max_area = 0
    index = 0
    while index < len(hist):
        if not stack or hist[index] >= hist[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = hist[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = hist[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
        max_area = max(max_area, area)
    return max_area


class Solution:
    def maxArea(self, M, n, m):
        max_area = 0
        hist = [0] * m
        for i in range(n):
            for j in range(m):
                if M[i][j] == 0:
                    hist[j] = 0
                else:
                    hist[j] += 1
            max_area = max(max_area, max_histogram_area(hist))
        return max_area


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
    ]
    r, c = len(matrix), len(matrix[0])
    res = Solution().maxArea(matrix, r, c)
    assert res == 8, f"Expected 8, got {res}"
    print(f"Maximum rectangle area: {res}")
