"""
Problem: Remove Consecutive Characters
Category: Strings
Pattern: Linear Scan / Adjacent Comparison

Time Complexity:  O(N) - Single pass through string
Space Complexity: O(N) - Result string construction
"""


def solve(S):
    if len(S) < 2:
        return S
    if S[0] != S[1]:
        return S[0] + solve(S[1:])
    return solve(S[1:])


class Solution:
    def removeConsecutiveCharacter(self, S):
        n = len(S)
        if n < 2:
            return S
        S = [i for i in S]
        j = 0
        for i in range(n):
            if S[j] != S[i]:
                j += 1
                S[j] = S[i]
        j += 1
        S = S[:j]
        return "".join(S)

        # return solve(S)


if __name__ == "__main__":
    ob = Solution()
    for s in ["aabb", "aabaa"]:
        print(f"Remove consecutive from '{s}': {ob.removeConsecutiveCharacter(s)}")
