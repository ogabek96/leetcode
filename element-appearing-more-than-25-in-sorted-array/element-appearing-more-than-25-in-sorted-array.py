class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        val = arr[0]
        cnt = 0
        for n in arr:
            if n == val:
                cnt+=1
            else:
                val = n
                cnt = 1
            if cnt > len(arr) / 4:
                return val
            