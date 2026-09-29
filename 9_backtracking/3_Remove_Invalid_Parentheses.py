"""
Problem: Remove Invalid Parentheses
Category: Backtracking
Pattern: Exhaustive State Exploration / Pruning

Time Complexity:  O(2^N) / Exponential
Space Complexity: O(N) - Recursion call stack
"""


def isParenthesis(c):
    return (c == "(") or (c == ")")


def isValidString(str):
    cnt = 0
    for i in range(len(str)):
        if str[i] == "(":
            cnt += 1
        elif str[i] == ")":
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []
        if len(s) == 0:
            return []

        visit = set()
        q = []
        level = False
        q.append(s)
        visit.add(s)
        while len(q):
            curr_str = q.pop(0)
            if isValidString(curr_str):
                res.append(curr_str)
                level = True
            if level:
                continue
            for i in range(len(curr_str)):
                if not isParenthesis(curr_str[i]):
                    continue
                temp = curr_str[0:i] + curr_str[i + 1 :]
                if temp not in visit:
                    q.append(temp)
                    visit.add(temp)
        return res
