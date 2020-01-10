# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        a = ListNode(-1)  
        b = a
        while l1 and l2:
            if l1.val <= l2.val:  
                b.next = l1
                l1 = l1.next  
            else:
                b.next = l2
                l2 = l2.next  
            b = b.next  

        b.next = l1 if l1 else l2
        return a.next
