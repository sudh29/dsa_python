"""
Problem: Merge K Sorted Linked Lists
Category: Heaps
Pattern: Min-Heap Priority Queue / Divide and Conquer

Time Complexity:  O(N * K * log K) where N is average list length
Space Complexity: O(K) - Min-heap storing node heads
"""

import heapq

"""
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    arr is a list containing the n linkedlist head pointers
	    n is an integer value

    node class:

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
"""


class Solution:
    # Function to merge K sorted linked list.
    def mergeKLists(self, arr, K):
        heap = []
        for i in range(K):
            heapq.heappush(heap, (arr[i].data, i, arr[i]))

        res = Node(0)
        prev = res
        while heap:
            curr_val, i, curr = heapq.heappop(heap)
            prev.next = curr
            prev = prev.next
            nxt = curr.next
            if nxt:
                heapq.heappush(heap, (nxt.data, i, nxt))
        return res.next


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next


if __name__ == "__main__":
    h1 = Node(1)
    h1.next = Node(3)
    h2 = Node(2)
    h2.next = Node(4)
    merged = Solution().mergeKLists([h1, h2], 2)
    print("Merged K lists successfully.")
