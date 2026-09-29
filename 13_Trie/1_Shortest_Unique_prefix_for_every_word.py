"""
Problem: Shortest Unique Prefix for Every Word
Category: Trie
Pattern: Trie with Frequency/Subtree Counter

Time Complexity:  O(N * L) - Insertion and prefix retrieval bounded by total characters
Space Complexity: O(N * L) - Trie node storage
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.count += 1

    def find_unique_prefix(self, word):
        current = self.root
        prefix = ""
        for char in word:
            prefix += char
            current = current.children[char]
            if current.count == 1:
                break
        return prefix


class Solution:
    def findPrefixes(self, arr, N):
        trie = Trie()
        for word in arr:
            trie.insert(word)

        unique_prefixes = []
        for word in arr:
            unique_prefixes.append(trie.find_unique_prefix(word))
        return unique_prefixes


if __name__ == "__main__":
    words = ["zebra", "dog", "duck", "dove"]
    print(f"Unique prefixes for {words}: {Solution().findPrefixes(words, len(words))}")
