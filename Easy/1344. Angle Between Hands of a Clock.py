class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        res = abs(hour * 30 + (0.5) * minutes - minutes * 6)
        return min(res, 360 - res)