"""
Problem: Longest Subsequence Such That Difference Between Adjacent Is One
Category: Dynamic Programming
Pattern: Hash Map / DP Lookup

Time Complexity:  O(N) - Linear pass querying dp[x-1] and dp[x+1]
Space Complexity: O(N) - Hash map storing max lengths
"""

from typing import List


class Solution:
    def longestSubseq(self, n: int, a: List[int]) -> int:
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if abs(a[i] - a[j]) == 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


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
    arr = [10, 9, 4, 5, 4, 8, 6]
    print(f"Longest diff-1 subsequence: {Solution().longestSubsequence(len(arr), arr)}")
