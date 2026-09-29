"""Tests for 8_greedy/ — Activity selection, fractional knapsack, platforms."""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "8_greedy" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestActivitySelection:
    def test_basic(self):
        mod = _load("0_Activity_Selection_Problem.py")
        sol = mod.Solution()
        start = [1, 3, 0, 5, 8, 5]
        end = [2, 4, 6, 7, 9, 9]
        assert sol.activitySelection(6, start, end) == 4

    def test_overlapping(self):
        mod = _load("0_Activity_Selection_Problem.py")
        sol = mod.Solution()
        assert sol.activitySelection(3, [1, 1, 1], [2, 2, 2]) == 1

    def test_non_overlapping(self):
        mod = _load("0_Activity_Selection_Problem.py")
        sol = mod.Solution()
        assert sol.activitySelection(3, [1, 3, 5], [2, 4, 6]) == 3


class TestFractionalKnapsack:
    def test_basic(self):
        mod = _load("4_Fractional_Knapsack_Problem.py")
        sol = mod.Solution()
        items = [mod.Item(60, 10), mod.Item(100, 20), mod.Item(120, 30)]
        result = sol.fractionalknapsack(50, items, 3)
        assert abs(result - 240.0) < 0.01

    def test_all_fit(self):
        mod = _load("4_Fractional_Knapsack_Problem.py")
        sol = mod.Solution()
        items = [mod.Item(10, 5), mod.Item(20, 10)]
        result = sol.fractionalknapsack(100, items, 2)
        assert abs(result - 30.0) < 0.01


class TestMinimumPlatforms:
    def test_basic(self):
        mod = _load("7_Minimum_Platforms_Problem.py")
        sol = mod.Solution()
        arr = [900, 940, 950, 1100, 1500, 1800]
        dep = [910, 1200, 1120, 1130, 1900, 2000]
        assert sol.minimumPlatform(6, arr[:], dep[:]) == 3

    def test_no_overlap(self):
        mod = _load("7_Minimum_Platforms_Problem.py")
        sol = mod.Solution()
        assert sol.minimumPlatform(2, [100, 300], [200, 400]) == 1

    def test_all_overlap(self):
        mod = _load("7_Minimum_Platforms_Problem.py")
        sol = mod.Solution()
        assert sol.minimumPlatform(3, [100, 100, 100], [200, 200, 200]) == 3
