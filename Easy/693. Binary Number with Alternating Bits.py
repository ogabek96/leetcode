class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = (bin(n)[2:])
        last = num[0]
        for n in num[1:]:
            if last == n:
                return False
            last = n
        return True