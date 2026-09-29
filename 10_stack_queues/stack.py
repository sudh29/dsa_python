"""
Problem: Stack
Category: Stacks & Queues
Pattern: LIFO / FIFO State Tracking / Monotonic Stack

Time Complexity:  O(N)
Space Complexity: O(N) - Auxiliary stack/queue
"""

# implement stack using deque LIFO

from collections import deque

q = deque()

q.append("a")
q.append("b")
q.append("c")

print("Queue")
print(q)
q.pop()
q.pop()
print("After pop")
print(q)
