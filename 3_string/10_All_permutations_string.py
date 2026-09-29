"""
Problem: Permutations of a Given String
Category: Strings
Pattern: Backtracking / Recursion

Time Complexity:  O(N * N!) - Generates all N! permutations of length N
Space Complexity: O(N!) - Storage for all generated permutations
"""


def permute(s):
    if len(s) == 0:
        return [""]
    permutations = []
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i + 1 :]
        for p in permute(remaining):
            permutations.append(char + p)
    return permutations


class Solution:
    def find_permutation(self, s):
        p = permute(s)
        p = list(set(p))
        return p


if __name__ == "__main__":
    ob = Solution()
    sample = "ABC"
    res = ob.find_permutation(sample)
    print(f"Permutations of {sample}: {res}")
