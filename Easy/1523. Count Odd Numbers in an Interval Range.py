class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        res+= int((high - low) / 2)
        if low & 1 != 0 or high & 1 != 0:
            res+=1
        return res