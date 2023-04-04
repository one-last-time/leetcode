# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getList(l):
    res = []
    while l is not None:
        res.append(l.val)
        l = l.next
    return res

def add(l1, l2):
    carry = 0;
    start = None
    l1 = getList(l1)
    l2 =getList(l2)
    while len(l1)!=len(l2):
        if(len(l1)<len(l2)):
            l1.append(0)
        else:
            l2.append(0)
    for i in range(len(l1)):
        sum = l1[i]+l2[i]+carry
        if sum > 9:
            carry = 1
            cur = ListNode(sum-10)
        else:
            carry = 0
            cur = ListNode(sum)
        if not start:
            start = cur
            last = cur
        else:
            last.next = cur
            last = cur
    if carry:
        last.next = ListNode(1)
    return start



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return add(l1, l2)