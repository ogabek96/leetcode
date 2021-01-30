import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for n in stones:
            heapq.heappush(heap, -1 * n)
        while len(heap) > 1:
            x = -1 * heapq.heappop(heap)
            y = -1 *  heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -1 * abs(y - x))
        if len(heap) == 0:
            return 0
        return  -1 * heap[0]