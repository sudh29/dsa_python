"""
Problem: Partition Array to K Subsets with Equal Sum
Category: Backtracking
Pattern: Backtracking / Subset Sum Partitioning with Pruning

Time Complexity:  O(K * 2^N) - Pruned recursive search
Space Complexity: O(N) - Visited array and recursion depth
"""


def solve(a, n, k, curr_sum, count, visited, sub_set_sum, idx):
    if sub_set_sum == curr_sum:
        if count == k - 2:
            return True
        return solve(a, n, k, 0, count + 1, visited, sub_set_sum, n - 1)

    for i in range(idx, -1, -1):
        if visited[i] or curr_sum + a[i] > sub_set_sum:
            continue
        visited[i] = True
        if solve(a, n, k, curr_sum + a[i], count, visited, sub_set_sum, i - 1):
            return True
        visited[i] = False
    return False


class Solution:
    def isKPartitionPossible(self, a, k):
        n = len(a)
        if k == 1:
            return True
        if n < k:
            return False
        total_sum = sum(a)
        if total_sum % k != 0:
            return False

        target_sum = total_sum // k
        visited = [False] * n
        curr_sum = 0
        count = 0
        return solve(a, n, k, curr_sum, count, visited, target_sum, n - 1)


if __name__ == "__main__":
    arr = [2, 1, 4, 5, 6]
    k = 3
    print(
        f"Can partition {arr} into {k} equal subsets: {Solution().isKPartitionPossible(arr, len(arr), k)}"
    )
