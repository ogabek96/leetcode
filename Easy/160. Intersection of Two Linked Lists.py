# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointA = headA
        pointB = headB
        while pointA != pointB:
            if pointA == None:
                pointA = headB
            else:
                pointA = pointA.next
            
            if pointB == None:
                pointB = headA
            else:
                pointB = pointB.next
        return pointA