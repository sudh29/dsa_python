"""
Problem: Construct Trie from Scratch
Category: Trie
Pattern: 26-Ary Prefix Tree

Time Complexity:  O(L) per insert/search where L is word length
Space Complexity: O(ALPHABET_SIZE * L * N) total trie node storage
"""


class Solution:
    # Function to insert string into TRIE.
    def insert(self, root, key):
        currentNode = root
        for char in key:
            index = ord(char) - ord("a")
            if not currentNode.children[index]:
                currentNode.children[index] = TrieNode()
            currentNode = currentNode.children[index]
        currentNode.isEndOfWord = True

    # Function to search for a string in TRIE.
    def search(self, root, key):
        currentNode = root
        for char in key:
            index = ord(char) - ord("a")
            if not currentNode.children[index]:
                return False
            currentNode = currentNode.children[index]
        return currentNode.isEndOfWord


class TrieNode:
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()


if __name__ == "__main__":
    t = Trie()
    sol = Solution()
    for w in ["the", "a", "there", "answer", "any", "by"]:
        sol.insert(t.root, w)
    assert sol.search(t.root, "the") is True
    assert sol.search(t.root, "these") is False
    print("Trie construct and search demo passed.")
