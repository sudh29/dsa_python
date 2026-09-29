"""
Problem: Fractional Knapsack Problem
Category: Greedy Algorithms
Pattern: Greedy Value-to-Weight Ratio Sorting

Time Complexity:  O(N log N) - Sorting items by value/weight ratio
Space Complexity: O(1) auxiliary space
"""


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, arr, n):
        # data = []
        # for i in range(n):
        #     data.append([arr[i].value,arr[i].weight, arr[i].value/arr[i].weight])
        # data = sorted(data,key=lambda x:x[2],reverse = True)
        arr.sort(key=lambda x: (x.value / x.weight), reverse=True)
        total_value = 0.0
        for item in arr:
            if item.weight <= W:
                W -= item.weight
                total_value += item.value
            else:
                total_value += item.value * (W / item.weight)
                break
        return total_value


if __name__ == "__main__":
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    w = 50
    print(f"Max value for weight {w}: {Solution().fractionalknapsack(w, items, len(items)):.2f}")
