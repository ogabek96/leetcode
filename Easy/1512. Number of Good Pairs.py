class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        leng = len(nums)
        res = 0
        for i in range(leng):
            for j in range(leng):
                if nums[i] == nums[j] and i < j:
                    res+=1
        return res