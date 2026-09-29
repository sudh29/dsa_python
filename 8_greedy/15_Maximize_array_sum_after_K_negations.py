"""
Problem: Maximize Sum After K Negations
Category: Greedy Algorithms
Pattern: Min-Heap / Sorting / Greedy Negation

Time Complexity:  O(N log N) - Sorting negative elements and smallest magnitude
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def maximizeSum(self, a, n, k):
        a.sort()
        i = 0
        for i in range(n):
            if k and a[i] < 0:
                a[i] *= -1
                k -= 1
                continue
            break
        if k == 0 or k % 2 == 0:
            return sum(a)

        if i == n:
            i -= 1
        if i != 0 and abs(a[i]) >= abs(a[i - 1]):
            i -= 1
        a[i] *= -1
        return sum(a)


if __name__ == "__main__":
    arr = [1, 2, -3, 4, 5]
    k = 1
    print(f"Max sum after {k} negations: {Solution().maximizeSum(arr, len(arr), k)}")
