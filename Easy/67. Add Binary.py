class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = a
        num2 = b
        lenMax = max(len(num1), len(num2))
        leng1 = len(num1)
        leng2 = len(num2)
        res = ""
        q = 0
        for i in range(0, lenMax):
            if leng1 - i - 1 >= 0:
                numb1 = int(num1[leng1 - i - 1])
            else:
                numb1 = 0
            if leng2 - i - 1 >= 0:
                numb2 = int(num2[leng2 - i - 1])
            else:
                numb2 = 0
            val = int(numb1) + int(numb2) + q
            res = str(val % 2) + res
            q = int(val / 2)
        if q > 0:
            res = str(q) + res
        return res