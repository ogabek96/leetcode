# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        result = 0
        while head != None:
            nums.append(head.val)
            head = head.next
        for i in range(len(nums)):
            result += nums[i] * (2 ** (len(nums) - i - 1))
        return result