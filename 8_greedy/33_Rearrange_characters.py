"""
Problem: Rearrange Characters in String
Category: Greedy Algorithms
Pattern: Max-Heap / Frequency Scheduling

Time Complexity:  O(N log(alphabet_size)) - Heap operations
Space Complexity: O(alphabet_size) - Frequency mapping
"""


class Solution:
    def rearrangeString(self, str):
        list_char = [0 for i in range(26)]
        for i in str:
            list_char[ord(i) - ord("a")] += 1

        max_freq, letter = 0, 0
        for i in range(len(list_char)):
            if list_char[i] > max_freq:
                max_freq = list_char[i]
                letter = i

        n = len(str)
        half_len = n // 2 if n % 2 == 0 else (n + 1) // 2
        if max_freq > half_len:
            return ""

        res = [""] * len(str)
        # Fill all even places with the majority character
        idx = 0
        while list_char[letter] > 0:
            res[idx] = chr(letter + ord("a"))
            idx += 2
            list_char[letter] -= 1
        # Fill the remaining characters
        for i in range(len(list_char)):
            while list_char[i] > 0:
                if idx >= len(res):
                    idx = 1
                res[idx] = chr(i + ord("a"))
                idx += 2
                list_char[i] -= 1
        return "".join(res)


if __name__ == "__main__":
    for s in ["geeksforgeeks", "bbbaba"]:
        print(f"Rearrange '{s}': {Solution().rearrangeString(s)}")
