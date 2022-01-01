class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(st):
            res = 0
            for s in st:
                res+=int(s)
            return res
        st = ""
        for ch in s:
            st+=str(ord(ch) - ord('a') + 1)
        while k > 0:
            st = transform(str(st))
            k-=1
        return st
