"""
Problem: Find Maximum Meetings in One Room
Category: Greedy Algorithms
Pattern: Activity Selection / Sort by End Time

Time Complexity:  O(N log N) - Sorting meetings by finish time
Space Complexity: O(N) - Storing meeting indices and end times
"""


class Solution:
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        data = [[start[i], end[i]] for i in range(n)]
        data = sorted(data, key=lambda x: x[1])
        res = 1
        temp = data[0]
        for i in range(1, n):
            if data[i][0] > temp[1]:
                res += 1
                temp = data[i]
        return res


if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    print(f"Max meetings: {Solution().maximumMeetings(len(start), start, end)}")
