class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxEl = nums[0]
        maxI = 0
        for i in range(len(nums)):
            if maxEl < nums[i]:
                maxEl = nums[i]
                maxI = i
        for n in nums:
            if n != maxEl and maxEl < n * 2:
                return -1
        return maxI