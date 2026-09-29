"""
Problem: Maximize Sum of Consecutive Differences in a Circular Array
Category: Greedy Algorithms
Pattern: Sorting / High-Low Interleaving

Time Complexity:  O(N log N) - Sorting the array
Space Complexity: O(1) auxiliary space
"""


def maxSum(arr, n):
    arr.sort()
    res = 0
    for i in range(n):
        res += abs(arr[i] - arr[n - 1 - i])
    return res

    # new_a = []
    # i=0
    # j=n-1
    # while i<j:
    #     new_a.append(arr[i])
    #     new_a.append(arr[j])
    #     i+=1
    #     j-=1
    # if len(new_a)!=n:
    #     new_a.insert(0,arr[i])
    # # print(new_a)
    # MaximumSum = 0
    # for i in range(0, n - 1):
    #     MaximumSum = MaximumSum + abs(new_a[i] - new_a[i + 1])

    # MaximumSum = MaximumSum + abs(new_a[0] - new_a[n-1])
    # return MaximumSum


if __name__ == "__main__":
    arr = [4, 2, 1, 8]
    print(f"Max circular consecutive differences sum: {maxSum(arr, len(arr))}")
