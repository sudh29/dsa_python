"""
Problem: Count Subarrays Product Less Than K
Category: Dynamic Programming
Pattern: Sliding Window / Two Pointers

Time Complexity:  O(N) - Each element added and removed at most once
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        start = 0
        prod = 1
        count = 0
        for end in range(n):
            prod *= a[end]
            while start <= end and prod >= k:
                prod //= a[start]
                start += 1
            count += end - start + 1
        return count

        # # Non contiguous
        # if k <= 1:
        #     return 0
        # dp = [0] * (k + 1)
        # result = 0
        # for j in range(1, n + 1):
        #     for i in range(k, 0, -1):
        #         if a[j - 1] <= i and a[j - 1] > 0:
        #             dp[i] += dp[i // a[j - 1]] + 1
        # return dp[k]


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    k = 10
    print(
        f"Subarrays with product < {k}: {Solution().countSubArrayProductLessThanK(arr, len(arr), k)}"
    )
