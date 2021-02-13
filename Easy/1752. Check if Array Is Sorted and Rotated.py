class Solution:
    def check(self, nums: List[int]) -> bool:
        r = sorted(nums)
        for start in range(len(nums)):
            if nums[start:] + nums[:start] == r:
                return True
        return False