"""Tests for 2_matrix/ — Spiral traversal, 2D search, rotation."""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "2_matrix" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestSpiralTraversal:
    def test_3x3(self):
        mod = _load("0_Spirally_traversing_a_matrix.py")
        sol = mod.Solution()
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert sol.spirallyTraverse(matrix, 3, 3) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_3x4(self):
        mod = _load("0_Spirally_traversing_a_matrix.py")
        sol = mod.Solution()
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        assert sol.spirallyTraverse(matrix, 3, 4) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    def test_1x1(self):
        mod = _load("0_Spirally_traversing_a_matrix.py")
        sol = mod.Solution()
        assert sol.spirallyTraverse([[42]], 1, 1) == [42]


class TestSearch2DMatrix:
    def test_found(self):
        mod = _load("1_Search_a_2D_Matrix.py")
        sol = mod.Solution()
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        assert sol.searchMatrix(matrix, 9) is True

    def test_not_found(self):
        mod = _load("1_Search_a_2D_Matrix.py")
        sol = mod.Solution()
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        assert sol.searchMatrix(matrix, 10) is False

    def test_corner(self):
        mod = _load("1_Search_a_2D_Matrix.py")
        sol = mod.Solution()
        matrix = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
        assert sol.searchMatrix(matrix, 1) is True
        assert sol.searchMatrix(matrix, 17) is True


class TestRotateMatrix:
    def test_3x3_anticlockwise(self):
        mod = _load("7_Rotate_by_90_degree_anti.py")
        sol = mod.Solution()
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = sol.rotateby90(a, 3)
        assert result == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

    def test_2x2(self):
        mod = _load("7_Rotate_by_90_degree_anti.py")
        sol = mod.Solution()
        a = [[1, 2], [3, 4]]
        result = sol.rotateby90(a, 2)
        assert result == [[2, 4], [1, 3]]
