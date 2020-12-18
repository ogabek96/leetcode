class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        return sorted(arr, key=self.num1)
    def num1(self, n):
        cnt = 0
        while n != 0:
            cnt+= n & 1
            n >>= 1
        return cnt