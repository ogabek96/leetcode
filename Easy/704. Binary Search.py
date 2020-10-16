class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums, target, 0, len(nums) - 1)
    def binary(self, nums, target, start, end):
        if start > end:
            return -1
        mid = int(start + (end - start) / 2)
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            return self.binary(nums,target,  mid + 1, end)
        else:
            return self.binary(nums,target, start, mid - 1)