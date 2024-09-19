class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
  if list1.val == None and list2.val == None:
    return

  l1 = list1.val
  l2 = list2.val

  if l1 > l2:
    None
    # mergeTwoLists(a, b.next)
  else:
    None
    # mergeTwoLists(a.next, b)











