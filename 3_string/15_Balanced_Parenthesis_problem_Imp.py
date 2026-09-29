"""
Problem: Parenthesis Checker
Category: Strings
Pattern: Stack / Bracket Matching

Time Complexity:  O(N) - Single pass through string
Space Complexity: O(N) - Stack for opening brackets
"""


# User function Template for python3


class Solution:
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        temp = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for i in x:
            if i in temp.keys():
                stack.append(i)
            else:
                if len(stack) == 0 or temp.get(stack.pop(), None) != i:
                    return False
        return True if len(stack) == 0 else False


if __name__ == "__main__":
    obj = Solution()
    for s in ["{([])}", "()", "([]"]:
        print(f"ispar('{s}') -> {obj.ispar(s)}")
