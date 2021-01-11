class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7:
            return ((1 + n) * n )// 2
        nums = n // 7
        a1 = 28
        an = a1 + 7 * (nums - 1)
        sn = (a1 + an) * nums // 2
        left = n - 7 * nums
        sn+= (1 + left) * left // 2 + left * nums
        return sn
