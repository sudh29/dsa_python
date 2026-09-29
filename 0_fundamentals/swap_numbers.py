"""
Problem: Swap Two Numbers Without Temporary Variable
Category: Fundamentals
Pattern: Bit Manipulation (XOR), Arithmetic Trick

Time Complexity:  O(1) - Constant-time operations
Space Complexity: O(1) - No extra space needed
"""


def swap_xor(a: int, b: int) -> tuple[int, int]:
    """Swaps two integers using XOR bit manipulation."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def swap_arithmetic(a: int, b: int) -> tuple[int, int]:
    """Swaps two integers using addition and subtraction."""
    a = a + b
    b = a - b
    a = a - b
    return a, b


def swap_pythonic(a: int, b: int) -> tuple[int, int]:
    """Swaps two integers using Python tuple unpacking (idiomatic)."""
    a, b = b, a
    return a, b


if __name__ == "__main__":
    test_cases = [
        (100, 50),
        (0, 0),
        (-5, 10),
        (1, 1),
    ]
    for a, b in test_cases:
        assert swap_xor(a, b) == (b, a), f"XOR swap failed for ({a}, {b})"
        assert swap_arithmetic(a, b) == (b, a), f"Arithmetic swap failed for ({a}, {b})"
        assert swap_pythonic(a, b) == (b, a), f"Pythonic swap failed for ({a}, {b})"
    print("All swap demonstrations passed!")
