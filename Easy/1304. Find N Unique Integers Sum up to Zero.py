class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(-(n // 2), 0, 1):
            res.append(i)
        for i in range(1, n // 2 + 1, 1):
            res.append(i)
        if n % 2 == 1:
            res.append(0)
        return res