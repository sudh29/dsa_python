"""
Problem: Max Length Chain of Pairs
Category: Dynamic Programming
Pattern: Greedy / Activity Selection on Intervals

Time Complexity:  O(N log N) - Sorting pairs by second element
Space Complexity: O(1) auxiliary space
"""

"""
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
"""


class Solution:
    def maxChainLen(self, P, n):
        # Greedy
        P.sort(key=lambda x: x.b)
        max_length = 1
        last_selected_end = P[0].b
        for i in range(1, n):
            if P[i].a > last_selected_end:
                max_length += 1
                last_selected_end = P[i].b
        return max_length

        # # DP
        # P.sort(key=lambda x: x.a)
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if P[j].b < P[i].a:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)


class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == "__main__":
    pairs = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
    print(f"Max length chain: {Solution().maxChainLen(pairs, len(pairs))}")
