"""
Problem: Minimum Characters Added at Front to Make String Palindrome
Category: Strings
Pattern: KMP Algorithm / LPS Array

Time Complexity:  O(N) - Building LPS array for concat string
Space Complexity: O(N) - LPS array storage
"""


def ispal(ip):
    i = 0
    j = len(ip) - 1
    while i < j:
        if ip[i] != ip[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def minChar(self, s):
        # res = 0
        # temp = [i for i in s]
        # while ispal(temp)==False:
        #     temp.pop()
        #     res+=1
        # return res

        augmented = s + "#" + s[::-1]
        # print(augmented)
        n = len(augmented)
        lps = [0] * n
        j = 0
        i = 1
        while i < n:
            if augmented[i] == augmented[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        # print(lps)
        return len(s) - lps[-1]


if __name__ == "__main__":
    ob = Solution()
    s = "AACECAAAA"
    print(f"Min characters to add for '{s}': {ob.minChar(s)}")
