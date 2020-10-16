class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num1 = A
        num2 = []
        while K >= 1:
            num2.insert(0, K % 10)
            K = int(K / 10)
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
            res = str(val % 10) + res
            q = int(val / 10)
        if q > 0:
            res = str(q) + res
        return res