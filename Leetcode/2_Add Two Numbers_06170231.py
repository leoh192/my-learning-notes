# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, a1, a2):
        if a1 == None:
            return a2
            
        if a2 == None:
            return a1
            
        sval = a1.val + a2.val
        if sval < 10:
            answer = ListNode(sval)
            answer.next = self.addTwoNumbers(a1.next, a2.next)
            return answer
        else:
            rval = a1.val + a2.val-10
            answer = ListNode(rval)
            answer.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(a1.next, a2.next))
            return answer
