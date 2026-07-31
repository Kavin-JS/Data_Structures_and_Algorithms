class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

def buildList(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head

def toList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    head = buildList([1,2,3,4,5])
    print(toList(removeNthFromEnd(head, 2)))
