"""
Problem: Maximum Product Subarray
Category: Arrays
Pattern: Two Pointers / Linear Scan

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    # Function to find maximum product subarray
    def maxProduct(self, arr, n):
        minprod = arr[0]
        maxprod = arr[0]
        res = arr[0]
        for i in range(1, n):
            min1 = minprod * arr[i]
            max1 = maxprod * arr[i]
            minprod = min(arr[i], min1, max1)
            maxprod = max(arr[i], max1, min1)
            res = max(res, maxprod)
        return res
