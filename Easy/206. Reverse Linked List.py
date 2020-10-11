# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        numbers = []
        if(head == None):
            return None
        while head != None:
            numbers.append(head.val)
            head = head.next
        first = ListNode(numbers[len(numbers) - 1])
        current = first
        for i in reversed(numbers[:-1]):
            newNode =  ListNode(i)
            current.next = newNode
            current = newNode
        return first