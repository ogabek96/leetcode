class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        for i in range(5, n + 1, 5):
            val = i
            while val % 5 == 0:
                val = val / 5
                res+=1
        return res