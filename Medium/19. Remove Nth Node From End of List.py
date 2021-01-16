# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cnt = 0
        fast = head
        slow = head
        while fast != None:
            if cnt > n:
                slow = slow.next
            fast = fast.next
            cnt+=1
        if cnt == n:
            return head.next
        if slow.next == None:
            return None
        slow.next = slow.next.next
        return head