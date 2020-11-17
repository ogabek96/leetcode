# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(-101)
        curr = newList       
        while l1 != None or l2 != None:
            num = None
            first = True
            if l1 != None and l2 != None:
                if l1.val < l2.val:
                    num = l1.val
                    first = True
                else:
                    num = l2.val
                    first = False
            if l1 == None:
                num = l2.val
                first = False
            if l2 == None:
                num = l1.val
                first = True
            curr.next = ListNode(num)
            curr = curr.next
            if first:
                l1 = l1.next
            else:
                l2 = l2.next
        return newList.next