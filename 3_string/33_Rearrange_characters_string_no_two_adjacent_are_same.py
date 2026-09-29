"""
Problem: Rearrange Characters Such That No Two Adjacent Are Same
Category: Strings
Pattern: Max-Heap / Greedy Frequency Placement

Time Complexity:  O(N log(alphabet_size)) - Heap operations bounded by alphabet size
Space Complexity: O(alphabet_size) - Frequency counts and heap
"""

from collections import Counter
import heapq


class Solution:
    def rearrangeString(self, S):
        char_count = Counter(S)
        max_heap = [(-freq, char) for char, freq in char_count.items()]
        heapq.heapify(max_heap)
        prev_char, prev_freq = None, 0
        result = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_char and prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            prev_char = char
            prev_freq = freq + 1
        rearranged_str = "".join(result)
        return rearranged_str if len(rearranged_str) == len(S) else "-1"


if __name__ == "__main__":
    ob = Solution()
    for s in ["aaabbc", "aa"]:
        print(f"Rearrange '{s}': {ob.rearrangeString(s)}")
