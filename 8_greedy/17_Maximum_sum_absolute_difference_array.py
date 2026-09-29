"""
Problem: Maximum Sum of Absolute Differences of an Array
Category: Greedy Algorithms
Pattern: Greedy Interleaving / Closed Form Formula

Time Complexity:  O(1) using closed-form formula
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def maxSum(self, N):
        if N == 1:
            return 1
        return (N * (N - 1)) // 2 + N // 2 - 1

        # a = [i+1 for i in range(N)]
        # new_a = []
        # i=0
        # j=N-1
        # while i<j:
        #     new_a.append(a[i])
        #     new_a.append(a[j])
        #     i+=1
        #     j-=1
        # if len(new_a)!=N:
        #     new_a.insert(0,a[i])
        # # print(new_a)
        # MaximumSum = 0
        # for i in range(0, N - 1):
        #     MaximumSum = MaximumSum + abs(new_a[i] - new_a[i + 1])
        # return MaximumSum


if __name__ == "__main__":
    for n in [4, 5, 6]:
        print(f"Max sum of differences for N={n}: {Solution().maxSum(n)}")
