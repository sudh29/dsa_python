def findMinInsertionsDP(str1, n):
    table = [[0 for i in range(n)] for i in range(n)]
    low, h, gap = 0, 0, 0
    for gap in range(1, n):
        low = 0
        for h in range(gap, n):
            if str1[low] == str1[h]:
                table[low][h] = table[low + 1][h - 1]
            else:
                table[low][h] = min(table[low][h - 1], table[low + 1][h]) + 1
            low += 1
    return table[0][n - 1]


class Solution:
    def countMin(self, Str):
        return findMinInsertionsDP(Str, len(Str))


def merge(ar):
    # Write your code here
    n = len(ar)
    s = 0
    e = n - 1
    res = 0
    while s <= e:
        if ar[s] == ar[e]:
            s += 1
            e -= 1
        elif ar[s] < ar[e]:
            s += 1
            ar[s] = ar[s] + ar[s - 1]
            res += 1
        else:
            e -= 1
            ar[e] = ar[e] = ar[e + 1]
            res += 1
    return res
