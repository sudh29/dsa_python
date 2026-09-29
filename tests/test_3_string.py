"""Tests for 3_string/ — Palindromes, Roman, Anagrams, Sliding Window."""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "3_string" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestReverseString:
    def test_basic(self):
        mod = _load("0_Reverse_String.py")
        sol = mod.Solution()
        s = list("hello")
        sol.reverseString(s)
        assert s == list("olleh")

    def test_even_length(self):
        mod = _load("0_Reverse_String.py")
        sol = mod.Solution()
        s = list("abcd")
        sol.reverseString(s)
        assert s == list("dcba")

    def test_single(self):
        mod = _load("0_Reverse_String.py")
        sol = mod.Solution()
        s = list("a")
        sol.reverseString(s)
        assert s == list("a")


class TestPalindrome:
    def test_palindrome(self):
        mod = _load("1_Palindrome_String.py")
        sol = mod.Solution()
        assert sol.isPalindrome("racecar") == 1

    def test_not_palindrome(self):
        mod = _load("1_Palindrome_String.py")
        sol = mod.Solution()
        assert sol.isPalindrome("hello") == 0

    def test_single_char(self):
        mod = _load("1_Palindrome_String.py")
        sol = mod.Solution()
        assert sol.isPalindrome("a") == 1

    def test_two_same(self):
        mod = _load("1_Palindrome_String.py")
        sol = mod.Solution()
        assert sol.isPalindrome("aa") == 1


class TestRomanToDecimal:
    def test_basic(self):
        mod = _load("25_Converting_Roman_Numerals_to_Decimal.py")
        sol = mod.Solution()
        assert sol.romanToDecimal("III") == 3

    def test_subtractive(self):
        mod = _load("25_Converting_Roman_Numerals_to_Decimal.py")
        sol = mod.Solution()
        assert sol.romanToDecimal("IV") == 4
        assert sol.romanToDecimal("IX") == 9
        assert sol.romanToDecimal("XL") == 40

    def test_complex(self):
        mod = _load("25_Converting_Roman_Numerals_to_Decimal.py")
        sol = mod.Solution()
        assert sol.romanToDecimal("MCMXCIV") == 1994

    def test_thousand(self):
        mod = _load("25_Converting_Roman_Numerals_to_Decimal.py")
        sol = mod.Solution()
        assert sol.romanToDecimal("M") == 1000


class TestLongestCommonPrefix:
    def test_common(self):
        mod = _load("26_Longest_Common_Prefix.py")
        sol = mod.Solution()
        assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

    def test_no_common(self):
        mod = _load("26_Longest_Common_Prefix.py")
        sol = mod.Solution()
        assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
