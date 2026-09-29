"""
Problem: Common Elements In All Rows Of A Given Matrix
Category: Matrix
Pattern: 2D Grid Traversal / Row-Column Scan

Time Complexity:  O(R * C)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def distinct(self, M, N):
        # code here
        c = 0
        temp = dict()
        for j in range(N):
            temp[M[0][j]] = 1

        for i in range(1, N):
            for j in range(N):
                if M[i][j] in temp.keys() and temp[M[i][j]] == i:
                    temp[M[i][j]] = i + 1
                    if i == N - 1:
                        c += 1
                        # print(mat[i][j], end = " ")
        return c
