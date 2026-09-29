"""
Problem: Array Subset Of Another Array
Category: Arrays
Pattern: Two Pointers / Linear Scan

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


def isSubset(a1, a2, n, m):
    temp = set()
    for i in range(n):
        temp.add(a1[i])
    for i in range(m):
        if a2[i] in temp:
            continue
        else:
            return "No"
    return "Yes"
