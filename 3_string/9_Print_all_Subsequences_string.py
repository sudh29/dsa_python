"""
Problem: Print All Subsequences of a String
Category: Strings
Pattern: Recursion / Pick-or-Don't-Pick

Time Complexity:  O(2^N) - Generates all 2^N possible subsequences
Space Complexity: O(2^N) - Storage for all subsequences
"""

VOWELS = {"a", "e", "i", "o", "u"}


def valid_str(s):
    return len(s) >= 2 and s[0] in VOWELS and s[-1] not in VOWELS


def solve(string, ans, res):
    if not string:
        if valid_str(ans):
            res.add(ans)
        return
    solve(string[1:], ans + string[0], res)
    solve(string[1:], ans, res)


class Solution:
    def allPossibleSubsequences(ob, S):
        res = set()
        solve(S, "", res)
        res = sorted(res)
        return res


if __name__ == "__main__":
    ob = Solution()
    s = "abc"
    print(f"All subsequences of '{s}': {ob.AllPossibleStrings(s)}")
