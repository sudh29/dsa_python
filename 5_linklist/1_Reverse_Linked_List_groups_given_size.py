class Solution:
    def reverse(self, head, k):
        curr = head
        prev = None
        nxt = None
        c = 0
        while curr and c < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            c += 1
        if nxt:
            head.next = self.reverse(nxt, k)
        return prev
