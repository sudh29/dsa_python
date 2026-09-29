"""
Problem: Check Anagrams
Category: Fundamentals
Pattern: Sorting / Character Frequency Comparison

Time Complexity:  O(n log n) - Dominated by sorting; O(n) with frequency counter
Space Complexity: O(n) - Sorted copies of the strings
"""

from collections import Counter


def are_anagrams_sort(a: str, b: str) -> bool:
    """Checks if two strings are anagrams using sorting."""
    if len(a) != len(b):
        return False
    return sorted(a.lower()) == sorted(b.lower())


def are_anagrams_counter(a: str, b: str) -> bool:
    """Checks if two strings are anagrams using character frequency (O(n) time)."""
    return Counter(a.lower()) == Counter(b.lower())


if __name__ == "__main__":
    test_cases = [
        ("dance", "cadne", True),
        ("sudh", "Rama", False),
        ("listen", "silent", True),
        ("hello", "world", False),
        ("", "", True),
        ("a", "a", True),
    ]
    for a, b, expected in test_cases:
        assert are_anagrams_sort(a, b) == expected, f"Sort failed for ({a}, {b})"
        assert are_anagrams_counter(a, b) == expected, f"Counter failed for ({a}, {b})"
    print("All anagram demonstrations passed!")
