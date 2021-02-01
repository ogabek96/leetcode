class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        for ch in s:
            if ch in hmap:
                hmap[ch]+=1
            else:
                hmap[ch] = 1
        values = hmap.values()
        res = 0
        for v in values:
            if v % 2 == 0:
                res+=v
            else:
                res+=v-1
        if len(s) > res:
            res+=1
        return res