class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

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
    print(toList(reverseList(head)))
