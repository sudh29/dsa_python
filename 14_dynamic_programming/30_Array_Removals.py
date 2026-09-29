# User function Template for python3


class Solution:
    def removals(self, arr, n, k):
        arr.sort()
        min_removals = float("inf")
        j = 0
        for i in range(n):
            while j < n and arr[j] - arr[i] <= k:
                j += 1
            min_removals = min(min_removals, n - (j - i))
        return min_removals


if __name__ == "__main__":
    arr = [1, 3, 4, 9, 10, 11, 12, 17, 20]
    ob = Solution()
    print(ob.removals(arr, len(arr), 4))
