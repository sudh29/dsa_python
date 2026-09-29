"""
Problem: Water Connection Problem
Category: Greedy Algorithms
Pattern: Connected Components / Path Traversal

Time Complexity:  O(N) - Each house has at most one incoming and outgoing pipe
Space Complexity: O(N) - Direct arrays for next houses and pipe diameters
"""


class Solution:
    def solve(self, n, p, a, b, d):
        # Create a dictionary to store the connections and their diameters
        # print(n,p,a,b,d)
        connections = {}
        for i, j, k in zip(a, b, d):
            connections[i] = (j, k)
        # print(connections)

        # Identify tanks and taps
        tanks = set(a) - set(b)
        tanks = sorted(tanks)
        # print(tanks)

        # Find pairs of tanks and taps with minimum diameter pipes
        pairs = []
        for tank in tanks:
            tap, min_diameter = connections[tank]
            while tap in set(b):
                if tap not in connections:  # Check if tap is not found in the connections
                    break
                min_diameter = min(min_diameter, connections[tap][1])
                tap = connections[tap][0]
            pairs.append([tank, tap, min_diameter])

        return pairs


if __name__ == "__main__":
    n, p = 9, 6
    a, b, d = [7, 5, 4, 2, 9, 3], [4, 9, 6, 8, 7, 1], [98, 72, 10, 22, 17, 66]
    print(f"Tanks and taps: {Solution().solve(n, p, a, b, d)}")
