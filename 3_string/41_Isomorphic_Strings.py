"""
Problem: Isomorphic Strings
Category: Strings
Pattern: Two-Way Hash Map / Bijection Check

Time Complexity:  O(N) - Single pass mapping characters between strings
Space Complexity: O(distinct_chars) - Character mapping dictionaries
"""


# User function Template for python3


class Solution:
    # Function to check if two strings are isomorphic.
    def areIsomorphic(self, str1, str2):
        if len(str1) != len(str2):
            return False
        map_str1_to_str2 = {}
        map_str2_to_str1 = {}
        for char1, char2 in zip(str1, str2):
            if char1 in map_str1_to_str2:
                if map_str1_to_str2[char1] != char2:
                    return False
            else:
                map_str1_to_str2[char1] = char2
            if char2 in map_str2_to_str1:
                if map_str2_to_str1[char2] != char1:
                    return False
            else:
                map_str2_to_str1[char2] = char1
        return True


if __name__ == "__main__":
    ob = Solution()
    print(f"areIsomorphic('aab', 'xxy') -> {ob.areIsomorphic('aab', 'xxy')}")
    print(f"areIsomorphic('aab', 'xyz') -> {ob.areIsomorphic('aab', 'xyz')}")
