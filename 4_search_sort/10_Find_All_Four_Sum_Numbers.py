"""
Problem: Find All Four Sum Numbers
Category: Searching & Sorting
Pattern: Binary Search / Divide & Conquer

Time Complexity:  O(N log N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    # arr: input list of integers
    # total_k: the quadruple sum required
    def fourSum(self, arr, total_k):
        arr.sort()  # Sort the array
        n = len(arr)
        res = []
        st1 = set()  # Using a set to avoid duplicate quadruples

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                k = j + 1
                right = n - 1
                while right > k:
                    current_sum = arr[i] + arr[j] + arr[k] + arr[right]
                    if current_sum == total_k:
                        temp = [arr[i], arr[j], arr[k], arr[right]]
                        st1.add(tuple(temp))  # Use a tuple to store in a set
                        k += 1
                        right -= 1
                    elif current_sum < total_k:
                        k += 1
                    else:
                        right -= 1

        # Converting the set back to a list of lists
        res = [list(item) for item in st1]
        return res
