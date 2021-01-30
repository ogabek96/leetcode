class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n + 1):
            if not self.isContainsZero(i) and not self.isContainsZero(n - i):
                return [i, n - i]
    def isContainsZero(self, n):
        return '0' in str(n)