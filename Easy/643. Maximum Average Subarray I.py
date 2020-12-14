class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = []
        if len(nums) == k:
            return sum(nums) / k
        prevSum = sum(nums[0: k])
        maxVal = prevSum
        for i in range(len(nums) - k):
            prevSum = prevSum - nums[i] + nums[i + k]
            maxVal = max(maxVal, prevSum)
        return maxVal / k