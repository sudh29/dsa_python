def isCircular(head):
    if head is None:
        return True
    curr = head
    while curr:
        if curr.next == head:
            return True
        curr = curr.next
    return False
