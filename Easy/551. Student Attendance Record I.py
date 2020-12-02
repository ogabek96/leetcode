class Solution:
    def checkRecord(self, s: str) -> bool:
        l = 0
        p = 0
        a = 0
        maxL = 0
        for ch in s:
            if ch == 'A':
                a+=1
            if ch == 'L':
                l+=1
            else:
                maxL = max(maxL, l)
                l = 0
        maxL = max(l, maxL)
        if a <= 1 and maxL <= 2:
            return True
        return False