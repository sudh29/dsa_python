"""
Problem: Minimum Platforms Required for Railway Station
Category: Greedy Algorithms
Pattern: Two Pointers / Sorting Arrivals & Departures

Time Complexity:  O(N log N) - Sorting arrival and departure times separately
Space Complexity: O(1) auxiliary space
"""


class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        plat_needed = 1
        result = 1
        # for i in range(n):
        #     plat_needed = 1
        #     for j in range(n):
        #         if i != j:
        #             if (arr[i] >= arr[j] and dep[j] >= arr[i]):
        #                 plat_needed += 1
        #     result = max(result, plat_needed)
        # return result

        arr.sort()
        dep.sort()
        i = 1
        j = 0
        # two pointer approach
        while i < n and j < n:
            # print(arr[i] , dep[j])
            if arr[i] > dep[j]:
                j += 1
                plat_needed -= 1
            else:
                plat_needed += 1
                i += 1
            result = max(result, plat_needed)
        return result


if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(f"Min platforms needed: {Solution().minimumPlatform(len(arr), arr, dep)}")
