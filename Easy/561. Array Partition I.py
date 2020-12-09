class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        minSum = 0
        for i in range(0, len(nums), 2):
            minSum += min(nums[i], nums[i + 1])
        return minSum