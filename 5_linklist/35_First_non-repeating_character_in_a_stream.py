"""
Problem: First Non-Repeating Character In A Stream
Category: Linked Lists
Pattern: Pointer Manipulation / Fast & Slow Pointers

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def FirstNonRepeating(self, A):
        res = []
        temp = []
        arr = [0] * 26

        for val in A:
            index = ord(val) - ord("a")
            arr[index] += 1
            if arr[index] == 1:
                temp.append(val)
            if arr[index] == 2:
                temp.remove(val)
            res.append(temp[0] if temp else "#")
        return "".join(res)
