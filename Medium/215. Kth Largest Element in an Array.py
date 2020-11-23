from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [i*(-1) for i in nums]
        heapify(nums)
        cnt = 0
        while cnt != k - 1:
            heappop(nums)
            cnt+=1
        return nums[0] * -1