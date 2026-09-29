"""
Problem: Longest Common Prefix
Category: Strings
Pattern: Two Pointers / Sliding Window

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        len(strs)
        min_len = min(len(s) for s in strs)
        lcp = ""
        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return lcp
            lcp += current_char
        return lcp
