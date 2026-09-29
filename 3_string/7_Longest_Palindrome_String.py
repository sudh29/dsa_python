"""
Problem: Longest Palindromic Substring
Category: Strings
Pattern: Manacher's Algorithm / Center Expansion

Time Complexity:  O(N) using Manacher's algorithm
Space Complexity: O(N) auxiliary space
"""


# Manacher’s Algorithm
class Solution:
    def longestPalinManacher(self, s):
        # Preprocess the string to add boundaries
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n  # Array to store the radius of the palindrome at each index
        C, R = 0, 0  # Center and right boundary of the current palindrome

        # Main loop to calculate palindrome lengths
        for i in range(1, n - 1):
            mirror = 2 * C - i  # Mirror index of `i` with respect to `C`

            # Use the mirror property or reset radius
            if i < R:
                P[i] = min(R - i, P[mirror])

            # Expand the palindrome centered at `i`
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # Update the center and right boundary
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum palindrome length and its center
        max_len, center_index = max((P[i], i) for i in range(1, n - 1))

        # Extract the longest palindromic substring
        start = (center_index - max_len) // 2  # Convert index in T back to original string
        return s[start : start + max_len]

    def longestPalin(self, s: str) -> str:
        # Center expansion approach (or delegate to Manacher)
        return self.longestPalinManacher(s)


if __name__ == "__main__":
    ob = Solution()
    for s in ["babad", "cbbd", "racecar"]:
        print(f"Longest palindrome in '{s}': {ob.longestPalin(s)}")
