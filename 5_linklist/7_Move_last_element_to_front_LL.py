class Solution:
    def moveToFront(self, head):
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr and curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        curr.next = head
        head = curr
        return head
