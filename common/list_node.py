"""
Problem: List Node
Category: Algorithms
Pattern: Algorithmic Pattern

Time Complexity:  O(N)
Space Complexity: O(1)
"""

from typing import Any, Self


class ListNode:
    """Standard singly-linked list node supporting both .val and .data conventions."""

    def __init__(self, val: int = 0, next: Self | None = None) -> None:
        self.val = val
        self.data = val  # Compatibility alias with GeeksforGeeks solutions
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.to_list() == other.to_list()

    @classmethod
    def from_list(cls, values: list[int]) -> Self | None:
        """Constructs a linked list from a Python list of integers."""
        if not values:
            return None
        head = cls(values[0])
        curr = head
        for v in values[1:]:
            curr.next = cls(v)
            curr = curr.next
        return head

    def to_list(self) -> list[int]:
        """Converts the linked list into a Python list of integers."""
        res: list[int] = []
        curr: ListNode | None = self
        visited: set[int] = set()
        while curr:
            if id(curr) in visited:  # Cycle guard
                break
            visited.add(id(curr))
            res.append(curr.val)
            curr = curr.next
        return res


class DoublyListNode:
    """Standard doubly-linked list node supporting next and prev pointers."""

    def __init__(
        self,
        val: int = 0,
        next: Self | None = None,
        prev: Self | None = None,
    ) -> None:
        self.val = val
        self.data = val
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"DoublyListNode({self.val})"

    @classmethod
    def from_list(cls, values: list[int]) -> Self | None:
        """Constructs a doubly-linked list from a Python list of integers."""
        if not values:
            return None
        head = cls(values[0])
        curr = head
        for v in values[1:]:
            node = cls(v, prev=curr)
            curr.next = node
            curr = node
        return head

    def to_list(self) -> list[int]:
        """Converts forward elements to a Python list."""
        res: list[int] = []
        curr: DoublyListNode | None = self
        visited: set[int] = set()
        while curr:
            if id(curr) in visited:
                break
            visited.add(id(curr))
            res.append(curr.val)
            curr = curr.next
        return res
