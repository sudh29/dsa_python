"""Tests for 5_linklist/ — Reversals, loop detection, middle node."""

import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common.list_node import ListNode


def _load(filename: str):
    spec = importlib.util.spec_from_file_location(
        filename.replace(".py", ""),
        Path(__file__).resolve().parent.parent / "5_linklist" / filename,
    )
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


class TestReverseLinkedList:
    def test_basic(self):
        mod = _load("0_Reverse_a_linked_list.py")
        sol = mod.Solution()
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = sol.reverseList(head)
        assert result.to_list() == [5, 4, 3, 2, 1]

    def test_single_node(self):
        mod = _load("0_Reverse_a_linked_list.py")
        sol = mod.Solution()
        head = ListNode(42)
        result = sol.reverseList(head)
        assert result.to_list() == [42]

    def test_two_nodes(self):
        mod = _load("0_Reverse_a_linked_list.py")
        sol = mod.Solution()
        head = ListNode.from_list([1, 2])
        result = sol.reverseList(head)
        assert result.to_list() == [2, 1]


class TestDetectLoop:
    def test_no_loop(self):
        mod = _load("2_Detect_Loop_in_linked_list.py")
        sol = mod.Solution()
        head = ListNode.from_list([1, 2, 3, 4, 5])
        assert sol.detectLoop(head) is False

    def test_with_loop(self):
        mod = _load("2_Detect_Loop_in_linked_list.py")
        sol = mod.Solution()
        head = ListNode.from_list([1, 2, 3, 4, 5])
        # Create loop: 5 → 3
        curr = head
        node3 = None
        while curr.next:
            if curr.val == 3:
                node3 = curr
            curr = curr.next
        curr.next = node3
        assert sol.detectLoop(head) is True

    def test_single_node_no_loop(self):
        mod = _load("2_Detect_Loop_in_linked_list.py")
        sol = mod.Solution()
        assert sol.detectLoop(ListNode(1)) is False


class TestMiddleOfLL:
    def test_odd_length(self):
        mod = _load("14_Middle_of_the_LL.py")
        sol = mod.Solution()
        head = mod.ListNode(1)
        head.next = mod.ListNode(2)
        head.next.next = mod.ListNode(3)
        head.next.next.next = mod.ListNode(4)
        head.next.next.next.next = mod.ListNode(5)
        assert sol.middleNode(head).val == 3

    def test_even_length(self):
        mod = _load("14_Middle_of_the_LL.py")
        sol = mod.Solution()
        head = mod.ListNode(1)
        head.next = mod.ListNode(2)
        head.next.next = mod.ListNode(3)
        head.next.next.next = mod.ListNode(4)
        assert sol.middleNode(head).val == 3

    def test_single(self):
        mod = _load("14_Middle_of_the_LL.py")
        sol = mod.Solution()
        head = mod.ListNode(42)
        assert sol.middleNode(head).val == 42
