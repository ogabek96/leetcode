class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = ""
        fr = ""
        if num < 0:
            num = abs(num)
            fr="-"
        while num >= 1:
            res= str(num % 7) + res
            num//=7
        return fr + res