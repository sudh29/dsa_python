"""
Problem: Boyer-Moore Pattern Searching (Bad Character Heuristic)
Category: Strings
Pattern: Bad Character Table / String Matching

Time Complexity:  O(N / M) best case, O(N * M) worst case
Space Complexity: O(alphabet_size) for bad character table
"""

NO_OF_CHARS = 256


def badCharHeuristic(string, size):
    badChar = [-1] * NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


def searchPattern(txt, pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            return True
            s += m - badChar[ord(txt[s + m])] if s + m < n else 1
        else:
            s += max(1, j - badChar[ord(txt[s + j])])
    return False


if __name__ == "__main__":
    txt = "ABAAABCD"
    pat = "ABC"
    print(f"Search '{pat}' in '{txt}': {searchPattern(txt, pat)}")
