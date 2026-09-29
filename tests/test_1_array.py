"""Tests for 1_array/ — Arrays, Two Pointers, Sliding Window, Kadane's, Prefix Sum."""

import importlib
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    """Dynamically imports a module from 1_array/."""
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "1_array" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestReverseArray:
    def test_basic(self):
        mod = _load("0_Reverse_the_array.py")
        sol = mod.Solution()
        assert sol.reverseWord("hello") == "olleh"

    def test_palindrome(self):
        mod = _load("0_Reverse_the_array.py")
        sol = mod.Solution()
        assert sol.reverseWord("racecar") == "racecar"

    def test_single_char(self):
        mod = _load("0_Reverse_the_array.py")
        sol = mod.Solution()
        assert sol.reverseWord("a") == "a"


class TestKadanesAlgorithm:
    def test_mixed_array(self):
        mod = _load("7_Kadanes_Algorithm.py")
        assert mod.max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7

    def test_all_negative(self):
        mod = _load("7_Kadanes_Algorithm.py")
        assert mod.max_subarray_sum([-5, -3, -1, -2]) == -1

    def test_single_element(self):
        mod = _load("7_Kadanes_Algorithm.py")
        assert mod.max_subarray_sum([42]) == 42

    def test_all_positive(self):
        mod = _load("7_Kadanes_Algorithm.py")
        assert mod.max_subarray_sum([1, 2, 3, 4]) == 10


class TestBestTimeBuySellStock:
    def test_increasing_prices(self):
        mod = _load("16_Best_Time_to_Buy_and_Sell_Stock.py")
        sol = mod.Solution()
        assert sol.maxProfit([1, 2, 3, 4, 5]) == 4

    def test_decreasing_prices(self):
        mod = _load("16_Best_Time_to_Buy_and_Sell_Stock.py")
        sol = mod.Solution()
        assert sol.maxProfit([5, 4, 3, 2, 1]) == 0

    def test_typical_case(self):
        mod = _load("16_Best_Time_to_Buy_and_Sell_Stock.py")
        sol = mod.Solution()
        assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5


class TestMergeIntervals:
    def test_overlapping(self):
        mod = _load("13_Merge_Intervals.py")
        sol = mod.Solution()
        assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
            [1, 6],
            [8, 10],
            [15, 18],
        ]

    def test_no_overlap(self):
        mod = _load("13_Merge_Intervals.py")
        sol = mod.Solution()
        assert sol.merge([[1, 2], [3, 4], [5, 6]]) == [[1, 2], [3, 4], [5, 6]]

    def test_single_interval(self):
        mod = _load("13_Merge_Intervals.py")
        sol = mod.Solution()
        assert sol.merge([[1, 5]]) == [[1, 5]]


class TestTrappingRainWater:
    def test_typical(self):
        mod = _load("28_Trapping_Rain_Water.py")
        sol = mod.Solution()
        assert sol.trappingWater([3, 0, 0, 2, 0, 4], 6) == 10

    def test_no_water(self):
        mod = _load("28_Trapping_Rain_Water.py")
        sol = mod.Solution()
        assert sol.trappingWater([1, 2, 3, 4, 5], 5) == 0

    def test_valley(self):
        mod = _load("28_Trapping_Rain_Water.py")
        sol = mod.Solution()
        assert sol.trappingWater([5, 0, 5], 3) == 5


class TestDutchNationalFlag:
    def test_mixed(self):
        mod = _load("3_Sort_an_array_of_0s,_1s_and_2s.py")
        sol = mod.Solution()
        arr = [0, 2, 1, 2, 0]
        sol.sort012(arr, len(arr))
        assert arr == [0, 0, 1, 2, 2]

    def test_already_sorted(self):
        mod = _load("3_Sort_an_array_of_0s,_1s_and_2s.py")
        sol = mod.Solution()
        arr = [0, 0, 1, 1, 2, 2]
        sol.sort012(arr, len(arr))
        assert arr == [0, 0, 1, 1, 2, 2]

    def test_single_element(self):
        mod = _load("3_Sort_an_array_of_0s,_1s_and_2s.py")
        sol = mod.Solution()
        arr = [1]
        sol.sort012(arr, 1)
        assert arr == [1]
