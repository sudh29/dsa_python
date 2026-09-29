"""
Problem: Reverse the Array / String
Category: Arrays
Pattern: Two Pointers / Symmetric Swapping

Time Complexity:  O(N) - Single pass swapping elements up to the midpoint
Space Complexity: O(N) - Storage for mutable character list
"""


class Solution:
    def reverseWord(self, str: str) -> str:
        n = len(str)
        str = list(str)
        for i in range(n // 2):
            str[i], str[n - i - 1] = str[n - i - 1], str[i]
        str = "".join(str)
        return str


if __name__ == "__main__":
    ob = Solution()
    sample = "Geeks"
    reversed_str = ob.reverseWord(sample)
    assert reversed_str == "skeeG", f"Expected 'skeeG', got {reversed_str}"
    print(f"Reverse '{sample}' -> '{reversed_str}'")
