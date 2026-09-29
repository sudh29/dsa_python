"""
Problem: Minimize the Heights II
Category: Arrays
Pattern: Greedy / Sorting

Time Complexity:  O(N log N) - Dominated by sorting the array
Space Complexity: O(1) auxiliary space
"""


class Solution:
    # Minimize the Heights I
    def getMinDiff_1(self, arr, n, k):
        if n == 1:
            return 0
        arr.sort()
        diff = arr[n - 1] - arr[0]
        for i in range(1, n):
            max_val = max(arr[i - 1] + k, arr[n - 1] - k)
            min_val = min(arr[0] + k, arr[i] - k)
            diff = min(diff, max_val - min_val)
        return diff

    # Minimize the Heights II
    def getMinDiff(self, arr, n, k):
        if n == 1:
            return 0
        arr.sort()
        diff = arr[n - 1] - arr[0]
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            max_val = max(arr[i - 1] + k, arr[n - 1] - k)
            min_val = min(arr[0] + k, arr[i] - k)
            diff = min(diff, max_val - min_val)
        return diff


if __name__ == "__main__":
    ob = Solution()
    sample_arr = [1, 5, 8, 10]
    sample_k = 2
    res = ob.getMinDiff(sample_arr, len(sample_arr), sample_k)
    assert res == 5, f"Expected 5, got {res}"
    print(f"Minimize heights for {sample_arr}, k={sample_k} -> {res}")
