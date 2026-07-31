class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    first, second = head, prev
    while second:
        n1 = first.next
        n2 = second.next
        first.next = second
        second.next = n1
        first = n1
        second = n2
    return head

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
    reorderList(head)
    print(toList(head))
