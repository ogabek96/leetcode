# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head != None:
           nums.append(head.val)
           head = head.next
        for i in range(len(nums)):
            if nums[i] != nums[-i - 1]:
                return False
        return True