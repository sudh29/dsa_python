"""Tests for 9_backtracking/ — N-Queens, Sudoku, Combinations, Tower of Hanoi."""

import importlib
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    """Dynamically imports a module from 9_backtracking/."""
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "9_backtracking" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestTowerOfHanoi:
    def test_one_disk(self):
        mod = _load("19_Tower_of_Hanoi.py")
        moves = mod.tower_of_hanoi(1, "A", "B", "C")
        assert len(moves) == 1
        assert moves[0] == "Move disk 1 from A to B"

    def test_three_disks(self):
        mod = _load("19_Tower_of_Hanoi.py")
        moves = mod.tower_of_hanoi(3, "A", "B", "C")
        assert len(moves) == 7  # 2^3 - 1

    def test_four_disks(self):
        mod = _load("19_Tower_of_Hanoi.py")
        moves = mod.tower_of_hanoi(4, "A", "B", "C")
        assert len(moves) == 15  # 2^4 - 1


class TestAllCombinations:
    def test_length_2(self):
        mod = _load("20_All_Combinations_String.py")
        result = mod.all_combinations(["1", "2", "3"], 2)
        assert len(result) == 9  # 3^2

    def test_length_0(self):
        mod = _load("20_All_Combinations_String.py")
        result = mod.all_combinations(["a", "b"], 0)
        assert result == [""]

    def test_binary(self):
        mod = _load("20_All_Combinations_String.py")
        result = mod.all_combinations(["0", "1"], 3)
        assert len(result) == 8  # 2^3


class TestPathFinder:
    def test_path_exists(self):
        mod = _load("21_Unique_Paths_Grid_Finder.py")
        matrix = [
            [1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ]
        path = mod.find_path(matrix, (0, 0), 5)
        assert path is not None
        assert path[0] == (0, 0)
        assert path[-1] == (4, 4)

    def test_no_path(self):
        mod = _load("21_Unique_Paths_Grid_Finder.py")
        blocked = [[1, 0], [0, 1]]
        assert mod.find_path(blocked, (0, 0), 2) is None

    def test_trivial(self):
        mod = _load("21_Unique_Paths_Grid_Finder.py")
        assert mod.find_path([[1]], (0, 0), 1) == [(0, 0)]


class TestNQueens:
    def test_4_queens(self):
        mod = _load("1_Printing_all_solutions_N-Queen_Problem.py")
        sol = mod.Solution()
        result = sol.nQueen(4)
        assert len(result) == 2  # 4-queens has exactly 2 solutions

    def test_1_queen(self):
        mod = _load("1_Printing_all_solutions_N-Queen_Problem.py")
        sol = mod.Solution()
        result = sol.nQueen(1)
        assert len(result) == 1
        assert result == [[1]]
