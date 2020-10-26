class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        empty = numBottles
        while empty >= numExchange:
            res+= int((empty) / numExchange)
            empty = int((empty) / numExchange) + empty % numExchange
        return res
            