import heapq
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        heap = []
        mem = {}
        heapq.heapify(heap)
        for n in nums:
            heapq.heappush(heap, -1 * n)
        result = [] 
        for n in nums:
            mem[-1 * heap[0]] = len(heap) - 1
            heapq.heappop(heap)
        for n in nums:
            result.append(mem[n])
        return result