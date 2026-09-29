"""
Problem: Tower of Hanoi
Category: Backtracking / Recursion
Pattern: Divide and Conquer (Recursive Decomposition)

Time Complexity:  O(2^n) - Requires 2^n - 1 moves for n disks
Space Complexity: O(n) - Recursion stack depth equals number of disks
"""


def tower_of_hanoi(n: int, source: str, target: str, auxiliary: str) -> list[str]:
    """Solves the Tower of Hanoi problem and returns the list of moves.

    Args:
        n: Number of disks to move.
        source: Name of the source peg.
        target: Name of the target peg.
        auxiliary: Name of the auxiliary peg.

    Returns:
        List of move descriptions.
    """
    moves: list[str] = []

    def _solve(num_disks: int, src: str, tgt: str, aux: str) -> None:
        if num_disks == 1:
            moves.append(f"Move disk 1 from {src} to {tgt}")
            return
        _solve(num_disks - 1, src, aux, tgt)
        moves.append(f"Move disk {num_disks} from {src} to {tgt}")
        _solve(num_disks - 1, aux, tgt, src)

    _solve(n, source, target, auxiliary)
    return moves


if __name__ == "__main__":
    # 3 disks: should require 2^3 - 1 = 7 moves
    moves = tower_of_hanoi(3, "A", "B", "C")
    assert len(moves) == 7, f"Expected 7 moves, got {len(moves)}"

    # 1 disk: should require 1 move
    moves_1 = tower_of_hanoi(1, "A", "B", "C")
    assert len(moves_1) == 1
    assert moves_1[0] == "Move disk 1 from A to B"

    # 4 disks: should require 2^4 - 1 = 15 moves
    moves_4 = tower_of_hanoi(4, "A", "B", "C")
    assert len(moves_4) == 15, f"Expected 15 moves, got {len(moves_4)}"

    print("All Tower of Hanoi demonstrations passed!")
