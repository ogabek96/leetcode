class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCon = 0
        soFar = 0
        for n in nums:
            if n == 1:
                soFar+=1
            else:
                maxCon=max(maxCon, soFar)
                soFar = 0
        return max(maxCon, soFar)