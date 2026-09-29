"""
Problem: Huffman Coding
Category: Greedy Algorithms
Pattern: Greedy Binary Tree / Priority Queue

Time Complexity:  O(N log N) - N insertions and deletions from min-heap
Space Complexity: O(N) - Storage for Huffman tree nodes and codes
"""

import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.huff = ""

    def __lt__(self, nxt):
        return self.freq < nxt.freq


def getList(ans, node, val=""):
    newval = val + str(node.huff)
    if node.left:
        getList(ans, node.left, newval)
    if node.right:
        getList(ans, node.right, newval)
    if not node.left and not node.right:
        ans.append(newval)


class Solution:
    def huffmanCodes(self, S, f, N):
        nodes = []
        for i in range(N):
            heapq.heappush(nodes, Node(S[i], f[i]))

        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            left.huff = "0"
            right.huff = "1"
            merged_node = Node(None, left.freq + right.freq)
            merged_node.left = left
            merged_node.right = right
            heapq.heappush(nodes, merged_node)

        ans = []
        getList(ans, nodes[0])
        return ans


if __name__ == "__main__":
    s = "abcdef"
    f = [5, 9, 12, 13, 16, 45]
    print(f"Huffman codes for {s}: {Solution().huffmanCodes(s, f, len(s))}")
