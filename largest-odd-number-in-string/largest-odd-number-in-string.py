class Solution:
    def largestOddNumber(self, num: str) -> str:
        pos = len(num) - 1
        while pos >= 0:
            if int(num[pos]) % 2 == 1:
                return num[:pos + 1]
            pos-=1
        if pos < 0:
            return ""