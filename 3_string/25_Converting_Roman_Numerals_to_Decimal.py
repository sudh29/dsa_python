"""
Problem: Roman Numerals to Decimal
Category: Strings
Pattern: Greedy / Right-to-Left Traversal

Time Complexity:  O(N) - Single pass through Roman numeral string
Space Complexity: O(1) - Fixed symbol lookup table
"""


class Solution:
    def romanToDecimal(self, s):
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            else:
                total += roman_values[s[i]]
        return total


if __name__ == "__main__":
    ob = Solution()
    for roman in ["III", "IV", "IX", "LVIII", "MCMXCIV"]:
        print(f"{roman} -> {ob.romanToDecimal(roman)}")
