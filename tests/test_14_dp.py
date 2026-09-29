"""Tests for 14_dynamic_programming/ — Knapsack, LCS, Coin Change, LIS."""

import importlib
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    """Dynamically imports a module from 14_dynamic_programming/."""
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "14_dynamic_programming" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestCoinChange:
    def test_basic(self):
        mod = _load("0_Coin_Change.py")
        sol = mod.Solution()
        assert sol.count([1, 2, 3], 3, 4) == 4  # {1,1,1,1}, {1,1,2}, {2,2}, {1,3}

    def test_single_coin(self):
        mod = _load("0_Coin_Change.py")
        sol = mod.Solution()
        assert sol.count([2], 1, 4) == 1  # Only {2,2}

    def test_impossible(self):
        mod = _load("0_Coin_Change.py")
        sol = mod.Solution()
        assert sol.count([5], 1, 3) == 0  # Can't make 3 with coins of 5


class TestKnapsack01:
    def test_basic(self):
        mod = _load("1_0-1_Knapsack_Problem.py")
        sol = mod.Solution()
        # val=[60,100,120], wt=[10,20,30], W=50 → max value = 220
        assert sol.knapSack(50, [10, 20, 30], [60, 100, 120], 3) == 220

    def test_zero_capacity(self):
        mod = _load("1_0-1_Knapsack_Problem.py")
        sol = mod.Solution()
        assert sol.knapSack(0, [1, 2], [10, 20], 2) == 0

    def test_single_item(self):
        mod = _load("1_0-1_Knapsack_Problem.py")
        sol = mod.Solution()
        assert sol.knapSack(10, [10], [60], 1) == 60


class TestLCS:
    def test_basic(self):
        mod = _load("13_Longest_Common_Subsequence.py")
        sol = mod.Solution()
        assert sol.lcs(7, 5, "ABCBDAB", "BDCAB") == 4  # BCAB

    def test_no_common(self):
        mod = _load("13_Longest_Common_Subsequence.py")
        sol = mod.Solution()
        assert sol.lcs(3, 3, "ABC", "DEF") == 0

    def test_identical(self):
        mod = _load("13_Longest_Common_Subsequence.py")
        sol = mod.Solution()
        assert sol.lcs(3, 3, "ABC", "ABC") == 3


class TestLIS:
    def test_basic(self):
        mod = _load("15_Longest_Increasing_Subsequence.py")
        sol = mod.Solution()
        assert sol.longestSubsequence([5, 8, 3, 7, 9, 1], 6) == 3  # [5, 7, 9] or [3, 7, 9]

    def test_sorted(self):
        mod = _load("15_Longest_Increasing_Subsequence.py")
        sol = mod.Solution()
        assert sol.longestSubsequence([1, 2, 3, 4, 5], 5) == 5

    def test_reverse_sorted(self):
        mod = _load("15_Longest_Increasing_Subsequence.py")
        sol = mod.Solution()
        assert sol.longestSubsequence([5, 4, 3, 2, 1], 5) == 1
