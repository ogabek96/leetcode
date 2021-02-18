class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        myset = set()
        for n in arr:
            if n * 2 in myset:
                return True
            elif n & 1 == 0 and n // 2 in myset:
                return True
            else:
                myset.add(n)
        return False