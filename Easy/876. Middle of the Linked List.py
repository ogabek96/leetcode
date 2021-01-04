import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cnt = 0
        curr = head
        while curr != None:
            curr = curr.next
            cnt+=1
        mid = cnt // 2
        curr = head
        cnt1 = 0
        while mid != cnt1:
            cnt1+=1
            curr = curr.next
        return curr