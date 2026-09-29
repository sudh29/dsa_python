"""Tests for 4_search_sort/ — Binary Search, Sorting Algorithms."""

import importlib
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    """Dynamically imports a module from 4_search_sort/."""
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "4_search_sort" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


# ─── Sorting Algorithm Tests ──────────────────────────────────────────

SORT_TEST_CASES = [
    ([5, 2, 6, 7, 2, 1, 0, 3], [0, 1, 2, 2, 3, 5, 6, 7]),
    ([], []),
    ([1], [1]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-3, -1, -2, 0], [-3, -2, -1, 0]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
]


class TestBubbleSort:
    @pytest.mark.parametrize("inp,expected", SORT_TEST_CASES)
    def test_sort(self, inp, expected):
        mod = _load("00_Bubble_Sort.py")
        assert mod.bubble_sort(inp[:]) == expected


class TestSelectionSort:
    @pytest.mark.parametrize("inp,expected", SORT_TEST_CASES)
    def test_sort(self, inp, expected):
        mod = _load("00_Selection_Sort.py")
        assert mod.selection_sort(inp[:]) == expected


class TestInsertionSort:
    @pytest.mark.parametrize("inp,expected", SORT_TEST_CASES)
    def test_sort(self, inp, expected):
        mod = _load("00_Insertion_Sort.py")
        assert mod.insertion_sort(inp[:]) == expected


class TestMergeSort:
    @pytest.mark.parametrize("inp,expected", SORT_TEST_CASES)
    def test_sort(self, inp, expected):
        mod = _load("00_Merge_Sort.py")
        assert mod.merge_sort(inp[:]) == expected


class TestQuickSort:
    @pytest.mark.parametrize("inp,expected", SORT_TEST_CASES)
    def test_sort(self, inp, expected):
        mod = _load("00_Quick_Sort.py")
        assert mod.quick_sort(inp[:]) == expected


class TestHeapSort:
    @pytest.mark.parametrize("inp,expected", SORT_TEST_CASES)
    def test_sort(self, inp, expected):
        mod = _load("00_Heap_Sort.py")
        assert mod.heap_sort(inp[:]) == expected


# ─── Search Algorithm Tests ───────────────────────────────────────────


class TestSearchInRotatedArray:
    def test_found(self):
        mod = _load("2_Search_in_a_rotated_sorted_array.py")
        sol = mod.Solution()
        assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_not_found(self):
        mod = _load("2_Search_in_a_rotated_sorted_array.py")
        sol = mod.Solution()
        assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_single_element(self):
        mod = _load("2_Search_in_a_rotated_sorted_array.py")
        sol = mod.Solution()
        assert sol.search([1], 1) == 0
        assert sol.search([1], 0) == -1


class TestCheckIfArraySorted:
    def test_sorted(self):
        mod = _load("29_Check_if_Array_is_Sorted.py")
        assert mod.is_sorted_recursive([1, 2, 3, 4, 5]) is True
        assert mod.is_sorted_iterative([1, 2, 3, 4, 5]) is True

    def test_unsorted(self):
        mod = _load("29_Check_if_Array_is_Sorted.py")
        assert mod.is_sorted_recursive([1, 5, 3, 2]) is False
        assert mod.is_sorted_iterative([1, 5, 3, 2]) is False

    def test_empty(self):
        mod = _load("29_Check_if_Array_is_Sorted.py")
        assert mod.is_sorted_recursive([]) is True
        assert mod.is_sorted_iterative([]) is True
