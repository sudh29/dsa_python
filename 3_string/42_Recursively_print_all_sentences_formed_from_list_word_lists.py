"""
Problem: Recursively Print All Sentences from List of Word Lists
Category: Strings
Pattern: Backtracking / DFS Cartesian Product

Time Complexity:  O(M^N) where N is number of rows and M is words per row
Space Complexity: O(N) - Recursion call stack depth
"""

from typing import List


class Solution:
    def sentences(self, L: List[List[str]]) -> List[List[str]]:
        def solve(index):
            if index == len(L):
                return [[]]
            partial_sentences = solve(index + 1)
            full_sentences = []
            for word in L[index]:
                for sentence in partial_sentences:
                    full_sentences.append([word] + sentence)
            return full_sentences

        # result = solve(0)
        # return [w for w in result]

        result = [""]
        for words in L:
            new_result = []
            for sentence in result:
                for word in words:
                    new_result.append(sentence + " " + word if sentence else word)
            result = new_result
        return [[w] for w in result]


if __name__ == "__main__":
    obj = Solution()
    matrix = [["you", "we"], ["have", "are"], ["sleep", "eat"]]
    print(f"Sentences: {obj.sentences(matrix)}")
