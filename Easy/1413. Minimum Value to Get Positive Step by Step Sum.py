class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal = 0
        startVal = 0
        for n in nums:
            startVal+=n
            minVal = min(startVal, minVal)
        return 1 - minVal if minVal < 0 else 1