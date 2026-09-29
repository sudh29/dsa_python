"""
Problem: Minimum Cost to Cut a Board into Squares
Category: Greedy Algorithms
Pattern: Greedy Sorting / Two Pointers

Time Complexity:  O(M log M + N log N) - Sorting horizontal and vertical costs
Space Complexity: O(1) auxiliary space
"""

from typing import List


class Solution:
    def minimumCostOfBreaking(self, X: List[int], Y: List[int], M: int, N: int) -> int:
        X.sort(reverse=True)
        Y.sort(reverse=True)

        vertical_count = 1
        horizontal_count = 1
        i, j = 0, 0
        ans = 0

        while i < M - 1 and j < N - 1:
            if X[i] > Y[j]:
                ans += X[i] * vertical_count
                horizontal_count += 1
                i += 1
            else:
                ans += Y[j] * horizontal_count
                vertical_count += 1
                j += 1

        while i < M - 1:
            ans += X[i] * vertical_count
            horizontal_count += 1
            i += 1

        while j < N - 1:
            ans += Y[j] * horizontal_count
            vertical_count += 1
            j += 1

        return ans


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, *args):
        return []

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    x = [2, 1, 3, 1, 4]
    y = [4, 1, 2]
    print(f"Min cost of breaking board: {Solution().minimumCostOfBreaking(x, y, 6, 4)}")
