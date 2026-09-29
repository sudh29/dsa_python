def reverseDLL(head):
    # return head after
    if head is None or head.next is None:
        return head
    curr = head
    while curr.next:
        curr = curr.next
    head = curr
    while curr:
        next = curr.next
        curr.next = curr.prev
        curr.prev = next
        curr = curr.next
    return head
