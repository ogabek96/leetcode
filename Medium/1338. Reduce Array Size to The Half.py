class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        m = {}
        for n in arr:
            if n not in m:
                m[n] = 1
            else:
                m[n]+=1
        s = reversed(sorted(m.values()))
        l = len(arr)
        cnt = 0
        for n in s:
            if l <= len(arr) / 2:
                return cnt
            else:
                l-=n
                cnt+=1
        return cnt
        