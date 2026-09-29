"""
Problem: Permutation Coefficient (P(n, k))
Category: Dynamic Programming
Pattern: Multiplicative Prefix DP

Time Complexity:  O(K) - Computing product n * (n-1) * ... * (n-k+1)
Space Complexity: O(1) auxiliary space
"""

MOD = 10**9 + 7


class Solution:
    def permutationCoeff(self, n, k):
        # if k > n:
        #     return 0
        # result = 1
        # for i in range(k):
        #     result = (result * (n - i)) % MOD
        # return result

        dp = [0 for _ in range(k + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(min(i, k), 0, -1):
                dp[j] = (dp[j] + (j * dp[j - 1]) % MOD) % MOD
        return dp[k]


if __name__ == "__main__":
    n, k = 10, 2
    print(f"P({n}, {k}): {Solution().permutationCoeff(n, k)}")
