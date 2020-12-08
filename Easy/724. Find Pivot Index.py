class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        allSum = sum(nums)
        sumSoFar = 0
        if len(nums) < 1:
            return -1
        for i in range(len(nums)):
            if allSum - nums[i] - sumSoFar == sumSoFar:
                return i
            sumSoFar+=nums[i]
        return -1