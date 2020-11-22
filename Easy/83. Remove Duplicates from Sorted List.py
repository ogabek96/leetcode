# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prevNode = head
        curr = head.next
        while curr != None:
            if prevNode.val == curr.val:
                prevNode.next = curr.next
            else:
                prevNode = curr
            curr = curr.next
        return head