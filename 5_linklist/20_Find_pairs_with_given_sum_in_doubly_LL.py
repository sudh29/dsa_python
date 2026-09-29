"""
Problem: Find Pairs With Given Sum In Doubly Linked List
Category: Linked Lists
Pattern: Pointer Manipulation / Fast & Slow Pointers

Time Complexity:  O(N)
Space Complexity: O(1) auxiliary space
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def findPairsWithGivenSum(self, target: int, head: Node | None) -> list[list[int]]:
        firstnode = head
        lastnode = head
        while lastnode.next:
            lastnode = lastnode.next

        res = []
        while firstnode != lastnode:
            temp_sum = firstnode.data + lastnode.data
            if temp_sum > target:
                lastnode = lastnode.prev
            elif temp_sum < target:
                firstnode = firstnode.next
            else:
                res.append((firstnode.data, lastnode.data))
                firstnode = firstnode.next
                if firstnode == lastnode:
                    break
                lastnode = lastnode.prev
        return res
