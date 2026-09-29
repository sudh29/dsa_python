from bisect import bisect_left


class Solution:
    def longestSubsequence(self, a, n):
        if n == 0:
            return 0

        # dp array to store the smallest tail of all increasing subsequences of various lengths
        dp = []

        for num in a:
            pos = bisect_left(dp, num)
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num

        return len(dp)


if __name__ == "__main__":
    a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    ob = Solution()
    print(ob.longestSubsequence(a, len(a)))
