class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2

    # Make sure l1 points to the smaller value node
    if l1.val > l2.val:
        l1, l2 = l2, l1

    l1.next = mergeTwoLists(l1.next, l2)
    return l1

def mergeKLists(lists):
    if not lists:
        return None

    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists) - interval, interval*2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2

    return lists[0]

# Test
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

result = mergeKLists([list1, list2, list3])

# Print result
while result:
    print(result.val, end=" -> ")
    result = result.next
