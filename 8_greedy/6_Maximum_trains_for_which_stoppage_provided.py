"""
Problem: Maximum Trains for Which Stoppage Can Be Provided
Category: Greedy Algorithms
Pattern: Activity Selection per Platform

Time Complexity:  O(N log N) - Sorting trains by departure time per platform
Space Complexity: O(N) - Segregating trains by platform number
"""


class Solution:
    def maxStop(self, n, m, trains):
        trains = sorted(trains, key=lambda x: x[1])
        platform = [-1] * (n + 1)
        count = 0
        for i in range(m):
            train = trains[i]
            if platform[train[2]] == -1:
                count += 1
                platform[train[2]] = train
            else:
                if platform[train[2]][1] <= train[0]:
                    platform[train[2]] = train
                    count += 1
        return count


if __name__ == "__main__":
    trains = [
        [1000, 1030, 1],
        [1010, 1030, 1],
        [1000, 1020, 2],
        [1030, 1230, 2],
        [1200, 1230, 3],
        [900, 1005, 1],
    ]
    print(f"Max trains stopped: {Solution().maxStop(3, len(trains), trains)}")
