"""
Problem: Longest Common Subsequence
Category: Strings
Pattern: Dynamic Programming (2D Grid)

Time Complexity:  O(N * M) - Filling DP matrix of size (N+1) x (M+1)
Space Complexity: O(N * M) - DP matrix storage
"""


def solve(n, m, X, Y, ans):
    if m == 0 or n == 0:
        return 0
    if ans[n][m] != -1:
        return ans[n][m]
    if X[n - 1] == Y[m - 1]:
        ans[n][m] = 1 + solve(n - 1, m - 1, X, Y, ans)
    else:
        ans[n][m] = max(solve(n - 1, m, X, Y, ans), solve(n, m - 1, X, Y, ans))
    return ans[n][m]


class Solution:
    def lcs(self, n, m, X, Y):
        # ans = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        # return solve(n, m, X, Y, ans)

        # DP
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if X[i - 1] == Y[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev, curr = curr, [0] * (m + 1)
        return prev[m]


if __name__ == "__main__":
    ob = Solution()
    s1, s2 = "ABCDGH", "AEDFHR"
    print(f"LCS of '{s1}' and '{s2}': {ob.lcs(len(s1), len(s2), s1, s2)}")
