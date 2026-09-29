"""
Problem: Find Smallest Number Given Number Digits Sum Digits
Category: Greedy Algorithms
Pattern: Greedy Choice / Sorting

Time Complexity:  O(N log N)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def smallestNumber(self, S, D):
        if 9 * D < S:
            return -1
        ans = [0 for i in range(D)]
        for i in range(D - 1, -1, -1):
            if S > 9:
                ans[i] = "9"
                S -= 9
            else:
                if i == 0:
                    ans[i] = str(S)
                else:
                    ans[i] = str(S - 1)
                    i -= 1
                    while i > 0:
                        ans[i] = "0"
                        i -= 1
                    ans[i] = "1"
                    break
        return "".join(ans)


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    ob = Solution()
    print(ob.smallestNumber(9, 2))  # Expected 18
    print(ob.smallestNumber(20, 3))  # Expected 299
