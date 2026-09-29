"""
Problem: Rearrange Characters Such That No Adjacent Are Same
Category: Heaps
Pattern: Max-Heap / Greedy Frequency Scheduling

Time Complexity:  O(N log(alphabet_size)) - Heap operations
Space Complexity: O(alphabet_size) - Frequency counts and heap
"""

import heapq


class Solution:
    def rearrangeString(self, str):
        char_count = {}
        for char in str:
            char_count[char] = char_count.get(char, 0) + 1

        heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(heap)
        res = []
        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            res.extend([char1, char2])
            if count1 < -1:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 < -1:
                heapq.heappush(heap, (count2 + 1, char2))
        if heap:
            count1, char1 = heapq.heappop(heap)
            if res and char1 == res[-1]:
                return "-1"
            res.append(char1)
        return "".join(res)


if __name__ == "__main__":
    ob = Solution()
    for s in ["geeksforgeeks", "bbbaba"]:
        print(f"Rearrange '{s}': {ob.rearrangeString(s)}")
