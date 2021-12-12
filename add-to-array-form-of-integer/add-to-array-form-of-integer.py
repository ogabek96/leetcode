class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if num[0] == 0 and k == 0:
            return [0]
        currnum = 0
        for n in num:
            currnum = currnum*10 + n
        res = []
        sums = currnum + k
        while sums > 0:
            res = [sums % 10] + res
            sums//=10
        return res