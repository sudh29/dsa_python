"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Pattern: Sliding Window (Variable Size) / Hash Map
Time Complexity: O(N)
Space Complexity: O(min(N, M)) where M is character set size

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring with unique characters.
        Uses sliding window with a dictionary storing the latest index of each character.
        """
        last_seen = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # If the character was seen inside the current window, shrink the window
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            # Update the latest index of the character
            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
    ]

    for text, expected in test_cases:
        result = sol.lengthOfLongestSubstring(text)
        print(f"String: {text!r} => Longest unique length: {result} (Expected: {expected})")
        assert result == expected, f"Failed for {text!r}: got {result}, expected {expected}"

    print("All test cases passed!")
