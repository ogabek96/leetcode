class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse = True)
        total = sum(nums)
        index = 0
        sumsofar = 0
        for n in nums:
            if sumsofar <= total:
                sumsofar+= n
                total-=n
                index+=1
            else:
                break
        return nums[0:index]
