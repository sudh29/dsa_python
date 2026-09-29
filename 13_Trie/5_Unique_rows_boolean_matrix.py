"""
Problem: Unique Rows in Boolean Matrix
Category: Trie
Pattern: Binary Trie (Alphabet size = 2)

Time Complexity:  O(R * C) - Traverses each boolean matrix cell once
Space Complexity: O(R * C) - Binary trie storage
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_row = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, row: List[int]) -> bool:
        current_node = self.root
        for num in row:
            if num not in current_node.children:
                current_node.children[num] = TrieNode()
            current_node = current_node.children[num]

        if current_node.is_end_of_row:
            return False
        else:
            current_node.is_end_of_row = True
            return True


class Solution:
    def uniqueRow(self, row: int, col: int, M: List[List[int]]) -> List[List[int]]:
        # res = []
        # unique_rows = set()
        # for i in range(row):
        #     row_tuple = tuple(M[i])
        #     if row_tuple not in unique_rows:
        #         unique_rows.add(row_tuple)
        #         res.append(M[i])
        # return res

        trie = Trie()
        res = []
        for i in range(row):
            if trie.insert(M[i]):
                res.append(M[i])
        return res


if __name__ == "__main__":
    matrix = [[1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1]]
    print(f"Unique rows: {Solution().uniqueRow(matrix, 3, 4)}")
