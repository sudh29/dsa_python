"""
Problem: Minimum Sum of Absolute Difference of Pairs of Two Arrays
Category: Greedy Algorithms
Pattern: Greedy Sorting / Parallel Matching

Time Complexity:  O(N log N) - Sorting both arrays
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def findMinSum(self, A, B, N):
        A.sort()
        B.sort()
        new = [abs(A[i] - B[i]) for i in range(N)]
        return sum(new)


if __name__ == "__main__":
    a = [4, 1, 8, 7]
    b = [2, 3, 6, 5]
    print(f"Min absolute difference sum: {Solution().findMinSum(a, b, len(a))}")
