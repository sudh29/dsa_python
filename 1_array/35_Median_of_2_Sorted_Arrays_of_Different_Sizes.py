"""
Problem: Median Of 2 Sorted Arrays Of Different Sizes
Category: Arrays
Pattern: Two Pointers / Linear Scan

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def MedianOfArrays(self, array1, array2):
        m = len(array1)
        n = len(array2)
        k = 0
        h = m + n
        i = 0
        j = 0
        temp = [0 for _ in range(h)]
        while k < h:
            if i < m and j < n and array1[i] <= array2[j]:
                temp[k] = array1[i]
                i += 1
            elif i < m and j < n and array1[i] > array2[j]:
                temp[k] = array2[j]
                j += 1
            elif i < m and j >= n:
                temp[k] = array1[i]
                i += 1
            elif i >= m and j < n:
                temp[k] = array2[j]
                j += 1
            k += 1
        v = temp
        n = h
        if n % 2 == 0:
            x = v[n // 2] + v[(n // 2) - 1]
            return x // 2 if x % 2 == 0 else x / 2
        else:
            return v[n // 2]
