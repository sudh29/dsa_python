"""
Problem: Min Number of Flips to Make Binary String Alternating
Category: Strings
Pattern: Greedy / Two-Pattern Comparison

Time Complexity:  O(N) - Linear pass comparing with '0101...' and '1010...'
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def minFlips(self, S):
        n = len(S)
        flips_starting_with_0 = 0
        flips_starting_with_1 = 0
        for i in range(n):
            expected_char_0 = "0" if i % 2 == 0 else "1"
            expected_char_1 = "1" if i % 2 == 0 else "0"
            if S[i] != expected_char_0:
                flips_starting_with_0 += 1
            if S[i] != expected_char_1:
                flips_starting_with_1 += 1
        return min(flips_starting_with_0, flips_starting_with_1)


if __name__ == "__main__":
    ob = Solution()
    s = "0001010111"
    print(f"Min flips for '{s}': {ob.minFlips(s)}")
