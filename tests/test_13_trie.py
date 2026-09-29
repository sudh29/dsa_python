"""Tests for 13_Trie/ — Trie insert, search, prefix."""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "13_Trie" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestTrieConstructFromScratch:
    def test_insert_and_search(self):
        mod = _load("0_Construct_trie_from_scratch.py")
        sol = mod.Solution()
        root = mod.TrieNode()
        sol.insert(root, "hello")
        sol.insert(root, "world")
        assert sol.search(root, "hello") is True
        assert sol.search(root, "world") is True

    def test_search_not_found(self):
        mod = _load("0_Construct_trie_from_scratch.py")
        sol = mod.Solution()
        root = mod.TrieNode()
        sol.insert(root, "hello")
        assert sol.search(root, "hel") is False  # Prefix, not full word
        assert sol.search(root, "xyz") is False

    def test_empty_trie(self):
        mod = _load("0_Construct_trie_from_scratch.py")
        sol = mod.Solution()
        root = mod.TrieNode()
        assert sol.search(root, "anything") is False

    def test_prefix_vs_word(self):
        mod = _load("0_Construct_trie_from_scratch.py")
        sol = mod.Solution()
        root = mod.TrieNode()
        sol.insert(root, "app")
        sol.insert(root, "apple")
        assert sol.search(root, "app") is True
        assert sol.search(root, "apple") is True
        assert sol.search(root, "appl") is False


class TestShortestUniquePrefix:
    def test_basic(self):
        mod = _load("1_Shortest_Unique_prefix_for_every_word.py")
        sol = mod.Solution()
        result = sol.findPrefixes(["zebra", "dog", "duck", "dove"], 4)
        assert result == ["z", "dog", "du", "dov"]
