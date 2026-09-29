"""Tests for 15_bit_manipulation/ — Set bits, power of two, non-repeating, power set."""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "15_bit_manipulation" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestNumberOf1Bits:
    def test_basic(self):
        mod = _load("0_Number_of_1_Bits.py")
        sol = mod.Solution()
        assert sol.setBits(11) == 3  # 1011

    def test_power_of_two(self):
        mod = _load("0_Number_of_1_Bits.py")
        sol = mod.Solution()
        assert sol.setBits(16) == 1  # 10000

    def test_all_ones(self):
        mod = _load("0_Number_of_1_Bits.py")
        sol = mod.Solution()
        assert sol.setBits(7) == 3  # 111

    def test_one(self):
        mod = _load("0_Number_of_1_Bits.py")
        sol = mod.Solution()
        assert sol.setBits(1) == 1


class TestNonRepeatingNumbers:
    def test_basic(self):
        mod = _load("1_Non_Repeating_Numbers.py")
        sol = mod.Solution()
        assert sol.singleNumber([1, 2, 3, 2, 1, 4]) == [3, 4]

    def test_two_elements(self):
        mod = _load("1_Non_Repeating_Numbers.py")
        sol = mod.Solution()
        assert sol.singleNumber([5, 10]) == [5, 10]


class TestIsPowerOfTwo:
    def test_powers(self):
        mod = _load("4_Is_power_of_two.py")
        sol = mod.Solution()
        assert sol.isPowerofTwo(1) is True
        assert sol.isPowerofTwo(2) is True
        assert sol.isPowerofTwo(4) is True
        assert sol.isPowerofTwo(16) is True
        assert sol.isPowerofTwo(1024) is True

    def test_not_powers(self):
        mod = _load("4_Is_power_of_two.py")
        sol = mod.Solution()
        assert sol.isPowerofTwo(0) is False
        assert sol.isPowerofTwo(3) is False
        assert sol.isPowerofTwo(6) is False
        assert sol.isPowerofTwo(-1) is False


class TestPowerSet:
    def test_basic(self):
        mod = _load("9_Power_Set.py")
        sol = mod.Solution()
        result = sol.AllPossibleStrings("abc")
        # Should have 2^3 - 1 = 7 non-empty subsets
        assert len(result) == 7
        assert "a" in result
        assert "abc" in result

    def test_two_chars(self):
        mod = _load("9_Power_Set.py")
        sol = mod.Solution()
        result = sol.AllPossibleStrings("ab")
        assert len(result) == 3
        assert sorted(result) == ["a", "ab", "b"]

    def test_single_char(self):
        mod = _load("9_Power_Set.py")
        sol = mod.Solution()
        result = sol.AllPossibleStrings("x")
        assert result == ["x"]
