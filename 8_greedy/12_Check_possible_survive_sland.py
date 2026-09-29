"""
Problem: Survival on an Island
Category: Greedy Algorithms
Pattern: Math / Greedy Buying

Time Complexity:  O(1) - Constant time arithmetic check
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def minimumDays(self, S, N, M):
        if M > N or (S > 6 and (N * 6) < (M * 7)):
            return -1
        total = S * M
        res = total // N
        if total % N > 0:
            res += 1
        return res


if __name__ == "__main__":
    s, n, m = 10, 16, 2
    print(f"Min days to buy food (S={s}, N={n}, M={m}): {Solution().minimumDays(s, n, m)}")
