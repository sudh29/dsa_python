"""
Problem: Median In A Row Wise Sorted Matrix
Category: Matrix
Pattern: 2D Grid Traversal / Row-Column Scan

Time Complexity:  O(R * C)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def median(self, matrix, r, c):
        # code here
        #     	temp=[]
        #     	for i in matrix:
        #     	    temp.extend(i)
        #     	temp.sort()
        #     	n=r*c
        #     	idx=(n+1)//2
        #         return temp[idx-1]

        start = 0
        end = 2000
        n = r * c
        while start <= end:
            mid = (end + start) // 2
            ans = 0
            for i in range(0, r, 1):
                low = 0
                h = c - 1
                while low <= h:
                    m = low + (h - low) // 2
                    if matrix[i][m] <= mid:
                        low = m + 1
                    else:
                        h = m - 1
                ans += low
            if ans <= n / 2:
                start = mid + 1
            else:
                end = mid - 1
        return start
