"""
Problem: Trie Node
Category: Algorithms
Pattern: Algorithmic Pattern

Time Complexity:  O(N)
Space Complexity: O(1)
"""


class TrieNode:
    """Standard Trie node with child map and end-of-word marker."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.count: int = 0
