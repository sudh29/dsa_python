"""Tests for 10_stack_queues/ — Parenthesis, next greater, stack reversal."""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "10_stack_queues" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestParenthesisChecker:
    def test_balanced(self):
        mod = _load("5_Parenthesis_Checker.py")
        sol = mod.Solution()
        assert sol.ispar("{[()]}") is True

    def test_unbalanced(self):
        mod = _load("5_Parenthesis_Checker.py")
        sol = mod.Solution()
        assert sol.ispar("{[(])}") is False

    def test_empty(self):
        mod = _load("5_Parenthesis_Checker.py")
        sol = mod.Solution()
        assert sol.ispar("") is True

    def test_single_open(self):
        mod = _load("5_Parenthesis_Checker.py")
        sol = mod.Solution()
        assert sol.ispar("(") is False

    def test_nested(self):
        mod = _load("5_Parenthesis_Checker.py")
        sol = mod.Solution()
        assert sol.ispar("((()))") is True


class TestNextGreaterElement:
    def test_basic(self):
        mod = _load("8_Find_the_next_Greater_element.py")
        sol = mod.Solution()
        assert sol.nextLargerElement([1, 3, 2, 4], 4) == [3, 4, 4, -1]

    def test_decreasing(self):
        mod = _load("8_Find_the_next_Greater_element.py")
        sol = mod.Solution()
        assert sol.nextLargerElement([4, 3, 2, 1], 4) == [-1, -1, -1, -1]

    def test_single(self):
        mod = _load("8_Find_the_next_Greater_element.py")
        sol = mod.Solution()
        assert sol.nextLargerElement([5], 1) == [-1]

    def test_equal_elements(self):
        mod = _load("8_Find_the_next_Greater_element.py")
        sol = mod.Solution()
        assert sol.nextLargerElement([1, 1, 1], 3) == [-1, -1, -1]


class TestReverseStringUsingStack:
    def test_basic(self):
        mod = _load("6_Reverse_a_String_using_Stack.py")
        assert mod.reverse("hello") == "olleh"

    def test_palindrome(self):
        mod = _load("6_Reverse_a_String_using_Stack.py")
        assert mod.reverse("aba") == "aba"

    def test_single(self):
        mod = _load("6_Reverse_a_String_using_Stack.py")
        assert mod.reverse("a") == "a"
