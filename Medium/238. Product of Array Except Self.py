class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []
        res = []
        prod = 1
        for i in range(len(nums)):
            res.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res