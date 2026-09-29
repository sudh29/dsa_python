"""
Problem: Print All Permutations of a String
Category: Backtracking
Pattern: Swap-based Backtracking

Time Complexity:  O(N * N!) - N! permutations of length N
Space Complexity: O(N) - Recursion call stack depth
"""


def solve(S, index, res):
    if index == len(S) - 1:
        res.append("".join(S))
        return
    seen = set()
    for i in range(index, len(S)):
        if S[i] not in seen:
            seen.add(S[i])
            S[index], S[i] = S[i], S[index]
            solve(S, index + 1, res)
            S[index], S[i] = S[i], S[index]


class Solution:
    def find_permutation(self, S):
        S = sorted(S)
        res = []
        solve(S, 0, res)
        return res


if __name__ == "__main__":
    s = "ABC"
    print(f"Permutations of '{s}': {Solution().find_permutation(s)}")
