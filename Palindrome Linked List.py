# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getList(self, l):
        res = []
        while l is not None:
            res.append(l.val)
            l = l.next
        return res

    def is_palindrome(self, lst):
        s = 0
        n = len(lst) - 1

        while s < n:
            if lst[s] != lst[n]:
                return False
            s += 1
            n -= 1
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = self.getList(head)
        return self.is_palindrome(lst)
