import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for n in nums:
            heapq.heappush(heap, n * (-1))
        return ((heapq.heappop(heap) * (-1)  - 1) * (heapq.heappop(heap) * (-1) - 1))