class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        a = log10(num) / log10(4)
        return floor(a) == ceil(a)