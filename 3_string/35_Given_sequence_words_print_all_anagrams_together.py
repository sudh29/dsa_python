"""
Problem: Print All Anagrams Together
Category: Strings
Pattern: Hash Map / Sorted Word Grouping

Time Complexity:  O(N * K log K) where N is word count and K is max word length
Space Complexity: O(N * K) - Storing grouped anagram lists
"""


class Solution:
    def Anagrams(self, words, n):
        """
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        """
        anagram_groups = dict()
        for word in words:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_groups.keys():
                anagram_groups[sorted_word] = [word]
            else:
                anagram_groups[sorted_word].append(word)
        return list(anagram_groups.values())


if __name__ == "__main__":
    ob = Solution()
    words = ["act", "god", "cat", "dog", "tac"]
    print(f"Grouped anagrams of {words}: {ob.Anagrams(words)}")
