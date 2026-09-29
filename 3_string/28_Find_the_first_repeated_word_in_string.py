"""
Problem: Find The First Repeated Word In String
Category: Strings
Pattern: Two Pointers / Sliding Window

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""

from collections import Counter


def firstRepeat(input):
    words = input.split(" ")
    dict = Counter(words)
    for key in words:
        if dict[key] > 1:
            print(key)
            return
    print(key)
    return


input = "Ravi had been saying that he had been there"
firstRepeat(input)


class Solution:
    def firstRepeatedWord(self, s):
        words = s.split()
        seen = set()
        for word in words:
            if word in seen:
                return word
            seen.add(word)
        return "-1"
