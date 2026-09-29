"""
Problem: Find Minimum and Maximum Element in an Array
Category: Arrays
Pattern: Linear Scan / Single Pass Comparison

Time Complexity:  O(N) - Single pass through the array with at most 2(N-1) comparisons
Space Complexity: O(1) auxiliary space
"""


def getMinMax(a, n):
    min_val = float("inf")
    max_val = float("-inf")
    for i in a:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return [min_val, max_val]


if __name__ == "__main__":
    demo_arr = [3, 2, 1, 56, 10000, 167]
    result = getMinMax(demo_arr, len(demo_arr))
    assert result == [1, 10000], f"Expected [1, 10000], got {result}"
    print(f"Min and Max of {demo_arr} -> {result}")
