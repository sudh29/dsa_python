"""
Problem: Next Permutation
Category: Strings
Pattern: Two Pointers / In-place Array Manipulation

Time Complexity:  O(N) - Linear scans and reversal
Space Complexity: O(1) - In-place permutation
"""


class Solution:
    def nextPermutation(self, N, arr):
        i = N - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i == -1:
            arr.reverse()
            return arr
        j = N - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1 :] = reversed(arr[i + 1 :])
        return arr


if __name__ == "__main__":
    ob = Solution()
    arr = [1, 2, 3]
    res = ob.nextPermutation(len(arr), arr)
    print(f"Next permutation of [1, 2, 3]: {res}")
