class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = []
        res = []
        for i in range(0, 9):
            for j in range(1, 9 - i):
                numbers.append(int("".join([str(k) for k in range(j, j+2 + i)])))
        for n in numbers:
            if low <= n and n <= high:
                res.append(n)
        return res