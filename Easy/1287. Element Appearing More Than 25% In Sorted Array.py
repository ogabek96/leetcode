class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0
        last = None
        num = len(arr) / 4
        for n in arr:
            if last == None:
                last = n
                count = 1
            else:
                if n == last:
                    count+=1
                else:
                    count = 1
                    last = n
            if count > num:
                return n