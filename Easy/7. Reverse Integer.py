class Solution:
    def reverse(self, x: int) -> int:
        res = ''
        cnt = 0
        dig = 1
        if x == 0:
            return 0
        if x < 0:
            dig = -1
            x = abs(x)
        while x > 0:
            res = res + str(x % 10)
            x = int(x / 10)
        res = int(res) * dig
        if -2 ** 31 > res or res > 2 ** 31 - 1:
            return 0
        return res