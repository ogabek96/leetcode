class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(len(nums)):
            if i < 2 or nums[index - 2] < nums[i]:
                nums[index] = nums[i]
                index+=1
        return index