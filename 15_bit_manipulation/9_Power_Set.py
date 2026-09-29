"""
Problem: Power Set
Category: Bit Manipulation
Pattern: Bitmask Enumeration from 0 to 2^N - 1

Time Complexity:  O(N * 2^N) - Generates all 2^N subsets
Space Complexity: O(1) auxiliary space (excluding result output)
"""


class Solution:
    def AllPossibleStrings(self, s):
        # Code here
        res = ""
        temp = []
        n = len(s)
        power_set_size = 2**n
        for i in range(1, power_set_size):
            for j in range(0, n):
                if (i & (1 << j)) > 0:
                    if s[j] != "":
                        res += s[j]
            temp.append(res)
            res = ""
        temp.sort()
        return temp
