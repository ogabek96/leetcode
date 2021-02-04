class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = 0
        res = -100001
        for i in range(len(nums)):
            maxSoFar+=nums[i]
            if maxSoFar > res:
                res=maxSoFar
            if maxSoFar < 0:
                maxSoFar = 0
        return res