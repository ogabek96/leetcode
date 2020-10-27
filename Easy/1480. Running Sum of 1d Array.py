class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prevSum = nums[0]
        for i in range(1, len(nums)):
            nums[i] += prevSum
            prevSum = nums[i]
        return nums