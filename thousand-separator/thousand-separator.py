class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        cnt = 0
        res = ""
        while n > 0:
            if cnt == 3:
                res = '.' + res
                cnt = 0
            num = n % 10
            n = n // 10
            res = str(num) + res
            cnt+=1
        return res