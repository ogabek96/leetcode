class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            gr = 0
            for n in nums:
                if n >= x:
                    gr+=1
            if x == gr:
                return x
        return -1