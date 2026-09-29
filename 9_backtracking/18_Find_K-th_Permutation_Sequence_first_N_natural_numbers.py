"""
Problem: Find K-th Permutation Sequence of First N Natural Numbers
Category: Backtracking
Pattern: Factorial Number System / Mathematical Selection

Time Complexity:  O(N^2) - Iterative extraction of digits via factorial blocks
Space Complexity: O(N) - Available digits array
"""


class Solution:
    def kthPermutation(self, n: int, k: int) -> str:
        # numbers = [str(i) for i in range(1,n+1)]
        # res = []
        # solve(numbers,0,res)
        # totalPermutations = factorial(n)
        # res = sorted(res)
        # if k > totalPermutations:
        #     k = k % totalPermutations
        # return res[k-1]

        totalPermutations = factorial(n)
        if k > totalPermutations:
            k = k % totalPermutations

        nums = [str(i) for i in range(1, n + 1)]
        result = []
        k -= 1
        while n > 0:
            index = k // factorial(n - 1)
            result.append(nums.pop(index))
            k %= factorial(n - 1)
            n -= 1
        return "".join(result)


def solve(nums, index, res):
    if index == len(nums) - 1:
        res.append("".join(nums))
        return
    seen = set()
    for i in range(index, len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
            nums[index], nums[i] = nums[i], nums[index]
            solve(nums, index + 1, res)
            nums[index], nums[i] = nums[i], nums[index]


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n, k = 4, 9
    print(f"{k}-th permutation for N={n}: {Solution().kthPermutation(n, k)}")
