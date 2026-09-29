"""
Problem: Phone Directory Search
Category: Trie
Pattern: Trie Prefix Auto-Complete

Time Complexity:  O(N * L + |query| * matches) - Building trie and querying prefixes
Space Complexity: O(N * L) - Trie node storage
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.contacts = set()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.contacts.add(word)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return sorted(node.contacts)


class Solution:
    def displayContacts(self, n, contact, s):
        trie = Trie()
        for con in contact:
            trie.insert(con)

        results = []
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            matches = trie.search(prefix)
            if matches:
                results.append(matches)
            else:
                results.append(["0"])
        return results


if __name__ == "__main__":
    contacts = ["geeikistest", "geeksforgeeks", "geeksfortest"]
    query = "geeips"
    print(
        f"Phone directory search for '{query}': {Solution().displayContacts(len(contacts), contacts, query)}"
    )
