"""
Problem: Maximize The Cut Segments
Category: Dynamic Programming
Pattern: 1D DP / Unbounded Rod Cutting

Time Complexity:  O(N) - Loop from 1 to N considering 3 cut lengths
Space Complexity: O(N) - 1D DP table
"""


class Solution:
    def maximizeTheCuts(self, n, x, y, z):
        dp = [-float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            if i >= x:
                dp[i] = max(dp[i], dp[i - x] + 1)
            if i >= y:
                dp[i] = max(dp[i], dp[i - y] + 1)
            if i >= z:
                dp[i] = max(dp[i], dp[i - z] + 1)

        return max(dp[n], 0)


if __name__ == "__main__":
    n, x, y, z = 4, 2, 1, 1
    print(
        f"Max cuts for length {n} with segments ({x}, {y}, {z}): {Solution().maximizeTheCuts(n, x, y, z)}"
    )
