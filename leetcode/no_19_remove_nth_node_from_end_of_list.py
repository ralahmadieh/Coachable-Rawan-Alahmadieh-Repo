class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head
    s, f = dummy, dummy

    for _ in range(n):
        f = f.next

    while f.next:
        f = f.next
        s = s.next

    s.next = s.next.next

    return dummy.next