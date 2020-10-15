# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(-1)
        current = root
        q = 0
        while l1 != None or l2 != None:
            if l1 != None:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2 != None:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            current.next = ListNode(int((num1 + num2 + q) % 10))
            current = current.next
            q = int((num1 + num2 + q) / 10)
        if q > 0:
            current.next = ListNode(int(q))
        return root.next