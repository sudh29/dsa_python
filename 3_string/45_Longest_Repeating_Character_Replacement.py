"""
Problem: Longest Repeating Character Replacement (LeetCode #424)
Pattern: Sliding Window (At Most K Replacements)
Time Complexity: O(N)
Space Complexity: O(1) (since uppercase English letters <= 26)

You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing at most k operations.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring with identical characters after at most k replacements.
        Condition: window_length - max_frequency <= k.
        """
        counts: dict[str, int] = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])

            # Current window length is (right - left + 1)
            # If characters needing replacement exceed k, shrink window from left
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("ABBB", 2, 4),
        ("AAAA", 2, 4),
        ("ABCDE", 1, 2),
    ]

    for s_str, k_val, expected in test_cases:
        result = sol.characterReplacement(s_str, k_val)
        print(f"s: {s_str!r}, k: {k_val} => Max Length: {result} (Expected: {expected})")
        assert result == expected, (
            f"Failed for s={s_str!r}, k={k_val}: got {result}, expected {expected}"
        )

    print("All test cases passed!")
