"""
Problem: Minimum Window Substring (LeetCode #76)
Pattern: Sliding Window / Frequency Map
Time Complexity: O(|S| + |T|)
Space Complexity: O(|S| + |T|)

Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum substring in s that contains all characters of t.
        Expands right to satisfy condition, contracts left to minimize length.
        """
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        required_chars = len(target_counts)

        window_counts: dict[str, int] = {}
        formed = 0

        # Store result tuple: (window_length, left, right)
        ans = (float("inf"), None, None)
        left = 0

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Contract window from the left as long as all required chars are satisfied
            while left <= right and formed == required_chars:
                window_len = right - left + 1
                if window_len < ans[0]:
                    ans = (window_len, left, right)

                left_char = s[left]
                window_counts[left_char] -= 1
                if (
                    left_char in target_counts
                    and window_counts[left_char] < target_counts[left_char]
                ):
                    formed -= 1

                left += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "b", "b"),
        ("cabwefgewcwaefgcf", "cae", "cwae"),
    ]

    for s_str, t_str, expected in test_cases:
        result = sol.minWindow(s_str, t_str)
        print(
            f"s: {s_str!r}, t: {t_str!r} => Min Window: {result!r} (Expected: {expected!r})"
        )
        assert result == expected, (
            f"Failed for s={s_str!r}, t={t_str!r}: got {result!r}, expected {expected!r}"
        )

    print("All test cases passed!")
