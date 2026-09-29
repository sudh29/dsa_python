"""
Problem: Combination Sum
Category: Backtracking
Pattern: Recursive Subset Generation / Pruning

Time Complexity:  O(2^T) where T is target / min element
Space Complexity: O(T) - Recursion depth bounded by target
"""


def solve(arr, target, current, idx, result):
    if target == 0:
        # if current[:] not in result:
        result.append(current[:])
        return
    for i in range(idx, len(arr)):
        if arr[i] > target:
            break
        if i > idx and arr[i] == arr[i - 1]:
            continue
        current.append(arr[i])
        solve(arr, target - arr[i], current, i, result)
        current.pop()


class Solution:
    # Function to return a list of indexes denoting the required
    # combinations whose sum is equal to given number.
    def combinationalSum(self, A, B):
        A.sort()
        result = []
        solve(A, B, [], 0, result)
        return result


if __name__ == "__main__":
    candidates = [2, 4, 6, 8]
    target = 8
    print(f"Combinations summing to {target}: {Solution().combinationalSum(candidates, target)}")
