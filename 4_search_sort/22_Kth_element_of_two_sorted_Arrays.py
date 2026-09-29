"""
Problem: Kth Element Of Two Sorted Arrays
Category: Searching & Sorting
Pattern: Binary Search / Divide & Conquer

Time Complexity:  O(N log N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        i = 0
        j = 0
        count = 0

        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                if count == k - 1:
                    return arr1[i]
                i += 1
            else:
                if count == k - 1:
                    return arr2[j]
                j += 1
            count += 1

        while i < n:
            if count == k - 1:
                return arr1[i]
            i += 1
            count += 1

        while j < m:
            if count == k - 1:
                return arr2[j]
            j += 1
            count += 1


# Example usage:
solution = Solution()
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
n = len(arr1)
m = len(arr2)
result = solution.kthElement(arr1, arr2, n, m, k)
print("The k-th element is:", result)
