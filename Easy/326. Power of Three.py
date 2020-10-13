class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        a = log10(n) / log10(3)
        return floor(a) == ceil(a)