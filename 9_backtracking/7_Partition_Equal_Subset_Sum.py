"""
Problem: Partition Equal Subset Sum
Category: Backtracking
Pattern: Subset Sum / 0-1 Knapsack DP

Time Complexity:  O(N * sum) - Pseudo-polynomial subset sum DP
Space Complexity: O(sum) - 1D boolean DP array
"""


# User function Template for Python3


def solve(arr, idx, curr_sum, target_sum):
    if curr_sum == target_sum:
        return True
    if curr_sum > target_sum or idx >= len(arr):
        return False
    if solve(arr, idx + 1, curr_sum + arr[idx], target_sum):
        return True
    if solve(arr, idx + 1, curr_sum, target_sum):
        return True
    return False


class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        return solve(arr, 0, 0, target_sum)


if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    print(f"Equal subset partition possible for {arr}: {Solution().equalPartition(len(arr), arr)}")
