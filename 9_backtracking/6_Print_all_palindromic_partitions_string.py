"""
Problem: Print All Palindromic Partitions of a String
Category: Backtracking
Pattern: DFS Partitioning / Palindrome Check

Time Complexity:  O(N * 2^N) - Generating all substring partitionings
Space Complexity: O(N) - Recursion stack and current partition list
"""


class Solution:
    # def allPalindromicPerms(self, S):
    #     self.res = set()
    #     self.solve(list(S))
    #     return sorted(list(self.res))

    # def solve(self,arr):
    #     self.res.add(tuple(arr))
    #     if len(arr)<=1:
    #         return
    #     for i in range(1,len(arr)):
    #         if arr[i-1]==arr[i]:
    #             new_arr = arr[:i-1]+ [arr[i-1]+arr[i]] + arr[i+1:]
    #             self.solve(new_arr)
    #         if i+1< len(arr) and arr[i-1]==arr[i+1]:
    #             new_arr = arr[:i-1]+ [arr[i-1]+arr[i]+arr[i+1]] + arr[i+2:]
    #             self.solve(new_arr)

    def allPalindromicPerms(self, S):
        self.result = []
        self.backtrack(S, [])
        return self.result

    def backtrack(self, s, path):
        if not s:
            self.result.append(path[:])
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                self.backtrack(s[i:], path + [prefix])

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    s = "geeks"
    print(f"Palindromic partitions of '{s}': {Solution().allPalindromicPerms(s)}")
