"""
Problem: Smallest Subset with Sum Greater Than All Other Elements
Category: Greedy Algorithms
Pattern: Greedy Sorting / Suffix Sum Comparison

Time Complexity:  O(N log N) - Sorting in descending order
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def minSubset(self, A, N):
        A.sort()
        i = 1
        A1 = sum(A[N - i : N])
        A2 = sum(A[0 : N - i])
        if A1 > A2:
            return i
        j = N - i
        while j > 0:
            j -= 1
            i += 1
            A1 += A[j]
            A2 -= A[j]
            if A1 > A2:
                return i
        return i


if __name__ == "__main__":
    arr = [2, 17, 7, 3]
    print(f"Min subset size: {Solution().minSubset(arr, len(arr))}")
