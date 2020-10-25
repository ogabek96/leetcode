# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = 0
        current = head
        lastVal = -1
        mem = {}
        for n in G:
            mem[n] = 1
        while current != None:
            if mem.get(current.val) != None:
                res+=1
            if mem.get(lastVal) != None and mem.get(current.val) != None:
                res-=1
            lastVal = current.val
            current = current.next 
        return res