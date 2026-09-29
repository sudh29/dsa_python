"""
Problem: Choose and Swap for Lexicographically Smallest String
Category: Greedy Algorithms
Pattern: Greedy First Occurrence / Set Lookup

Time Complexity:  O(N * 26) - Scanning first occurrences of characters
Space Complexity: O(26) - Character set lookup
"""

MAX = 256


class Solution:
    def chooseandswap(self, A):
        A = [i for i in A]
        n = len(A)
        i, j = 0, 0
        chk = [-1 for i in range(MAX)]
        for i in range(n):
            if chk[ord(A[i])] == -1:
                chk[ord(A[i])] = i
        for i in range(n):
            flag = False
            for j in range(ord(A[i])):
                if chk[j] > chk[ord(A[i])]:
                    flag = True
                    break
            if flag:
                break
        if i < n - 1:
            ch1 = A[i]
            ch2 = chr(j)
            for i in range(n):
                if A[i] == ch1:
                    A[i] = ch2
                elif A[i] == ch2:
                    A[i] = ch1
        return "".join(A)


if __name__ == "__main__":
    s = "ccad"
    print(f"Choose and swap '{s}': {Solution().chooseandswap(s)}")
