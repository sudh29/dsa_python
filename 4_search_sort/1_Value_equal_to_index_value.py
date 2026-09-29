"""
Problem: Value Equal To Index Value
Category: Searching & Sorting
Pattern: Binary Search / Divide & Conquer

Time Complexity:  O(N log N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def valueEqualToIndex(self, arr, n):
        res = []
        for i in range(n):
            if i + 1 == arr[i]:
                res.append(arr[i])
        return res
