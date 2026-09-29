"""
Problem: Queue
Category: Stacks & Queues
Pattern: LIFO / FIFO State Tracking / Monotonic Stack

Time Complexity:  O(N)
Space Complexity: O(N) - Auxiliary stack/queue
"""

# queue implementation

from collections import deque

q = deque()

q.append("a")
q.append("b")
q.append("c")

print("Queue")
print(q)
q.popleft()
q.popleft()
print("After deque")
print(q)
