class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums) * (len(nums) + 1) / 2
        return int(s - sum(nums))