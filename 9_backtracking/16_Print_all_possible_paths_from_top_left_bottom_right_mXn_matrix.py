"""
Problem: Count All Possible Paths from Top-Left to Bottom-Right of Matrix
Category: Backtracking
Pattern: Dynamic Programming / Combinatorics (Right & Down)

Time Complexity:  O(M * N) - 2D grid filling or O(min(M, N)) combinatorics
Space Complexity: O(N) - 1D DP array
"""


def binomialCoefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def solve(m, n, path, i, j, res):
    if i == m - 1 and j == n - 1:
        res.append(path)
        return
    if i < 0 or i >= m or j < 0 or j >= n:
        return
    if j + 1 < n:
        solve(m, n, path + "R", i, j + 1, res)
    if i + 1 < m:
        solve(m, n, path + "D", i + 1, j, res)


class Solution:
    def numberOfPaths(self, m, n):
        # 		# find all paths
        # 		res=[]
        # 		solve(m,n,'',0,0,res)
        # 		return len(res)

        #         # Count number of paths
        #         if(m == 1 or n == 1):
        #             return 1
        #         return self.numberOfPaths(m-1, n) + self.numberOfPaths(m, n-1)

        num_paths = binomialCoefficient(m + n - 2, m - 1)
        return num_paths % (10**9 + 7)


if __name__ == "__main__":
    m, n = 3, 3
    print(f"Paths in {m}x{n} grid: {Solution().numberOfPaths(m, n)}")
