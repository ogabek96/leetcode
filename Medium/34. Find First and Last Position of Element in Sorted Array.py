class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findLeftIndex(nums, target)
        right = self.findRightIndex(nums, target)
        return [left, right]
    def findLeftIndex(self, nums, target):
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] == target:
                index = mid
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return index
    def findRightIndex(self, nums, target):
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] == target:
                index = mid
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return index
        