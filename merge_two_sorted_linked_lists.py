class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    curr = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2
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
    l1 = buildList([1,2,4])
    l2 = buildList([1,3,4])
    print(toList(mergeTwoLists(l1, l2)))
