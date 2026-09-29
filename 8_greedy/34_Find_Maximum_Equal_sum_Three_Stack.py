"""
Problem: Find Maximum Equal Sum of Three Stacks
Category: Greedy Algorithms
Pattern: Greedy Top Removal / Three Pointers

Time Complexity:  O(N1 + N2 + N3) - Sum computation and linear pops
Space Complexity: O(1) auxiliary space
"""

from typing import List


class Solution:
    def maxEqualSum(
        self, N1: int, N2: int, N3: int, S1: List[int], S2: List[int], S3: List[int]
    ) -> int:
        # code here
        # print(N1,N2,N3,S1,S2,S3)
        sum1, sum2, sum3 = sum(S1), sum(S2), sum(S3)
        i, j, k = 0, 0, 0
        while True:
            if sum1 == sum2 and sum2 == sum3:
                return sum1
            else:
                max_sum = max(sum1, sum2, sum3)
                if max_sum == sum1:
                    sum1 -= S1[i]
                    i += 1
                elif max_sum == sum2:
                    sum2 -= S2[j]
                    j += 1
                elif max_sum == sum3:
                    sum3 -= S3[k]
                    k += 1
        return 0


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, *args):
        return []

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    s1, s2, s3 = [3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]
    print(f"Max equal sum: {Solution().maxEqualSum(len(s1), len(s2), len(s3), s1, s2, s3)}")
