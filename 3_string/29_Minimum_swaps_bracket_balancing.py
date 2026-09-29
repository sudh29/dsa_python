"""
Problem: Minimum Swaps for Bracket Balancing
Category: Strings
Pattern: Two Pointers / Greedy Swap

Time Complexity:  O(N) - Single pass through bracket positions
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def minimumNumberOfSwaps(self, S):
        open_count, close_count, UB, swaps = 0, 0, 0, 0
        for char in S:
            if char == "[":
                open_count += 1
                if UB > 0:
                    swaps += UB
                    UB -= 1
            else:
                close_count += 1
                UB = close_count - open_count
        return swaps


if __name__ == "__main__":
    ob = Solution()
    s = "[]][]["
    print(f"Min swaps for '{s}': {ob.minimumNumberOfSwaps(s)}")
