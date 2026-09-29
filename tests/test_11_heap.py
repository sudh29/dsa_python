"""Tests for 11_heap/ — Min/max heap, top-k."""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "11_heap" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestMaxMinHeap:
    def test_max_heapify(self):
        mod = _load("0_Implement_Maxheap_MinHeap_arrays_recursion.py")
        arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
        n = len(arr)
        mod.max_buildHeap(arr, n)
        # Root should be max element
        assert arr[0] == 17

    def test_min_heapify(self):
        mod = _load("0_Implement_Maxheap_MinHeap_arrays_recursion.py")
        arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
        n = len(arr)
        mod.min_buildHeap(arr, n)
        # Root should be min element
        assert arr[0] == 1

    def test_single_element(self):
        mod = _load("0_Implement_Maxheap_MinHeap_arrays_recursion.py")
        arr = [42]
        mod.max_buildHeap(arr, 1)
        assert arr[0] == 42


class TestKLargestElements:
    def test_basic(self):
        mod = _load("3_k_largest_element_array.py")
        sol = mod.Solution()
        result = sol.kLargest([12, 5, 787, 1, 23], 5, 2)
        assert result == [787, 23]

    def test_k_equals_n(self):
        mod = _load("3_k_largest_element_array.py")
        sol = mod.Solution()
        result = sol.kLargest([3, 1, 2], 3, 3)
        assert result == [3, 2, 1]

    def test_k_equals_1(self):
        mod = _load("3_k_largest_element_array.py")
        sol = mod.Solution()
        result = sol.kLargest([5, 10, 3], 3, 1)
        assert result == [10]
