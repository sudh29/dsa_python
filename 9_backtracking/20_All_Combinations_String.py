"""
Problem: All Combinations of a String (with Repetition)
Category: Backtracking
Pattern: Recursive Enumeration with Repetition

Time Complexity:  O(n^k) - n choices at each of k positions
Space Complexity: O(k) - Recursion depth equals combination length k
"""


def all_combinations(arr: list[str], k: int) -> list[str]:
    """Generates all combinations of length k from the given characters with repetition.

    Args:
        arr: List of characters to choose from.
        k: Length of each combination.

    Returns:
        List of all k-length combinations.
    """
    result: list[str] = []

    def _backtrack(prefix: str, remaining: int) -> None:
        if remaining == 0:
            result.append(prefix)
            return
        for ch in arr:
            _backtrack(prefix + ch, remaining - 1)

    _backtrack("", k)
    return result


if __name__ == "__main__":
    # 3 characters, length 2: 3^2 = 9 combinations
    result1 = all_combinations(["1", "2", "3"], 2)
    assert len(result1) == 9, f"Expected 9 combinations, got {len(result1)}"
    assert "11" in result1
    assert "23" in result1

    # 2 characters, length 3: 2^3 = 8 combinations
    result2 = all_combinations(["a", "b"], 3)
    assert len(result2) == 8
    assert "aaa" in result2
    assert "bbb" in result2

    # Length 0: only empty string
    result3 = all_combinations(["a", "b"], 0)
    assert result3 == [""]

    print("All string combinations demonstrations passed!")
