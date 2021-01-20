class Solution:
    def countLargestGroup(self, n: int) -> int:
        hmap = {}
        maxGr = 0
        for i in range(1, n + 1):
            d = self.digSum(i)
            if d in hmap:
                hmap[d]+=1
            else:
                hmap[d] = 1
            maxGr = max(maxGr, hmap[d])
        res = 0
        for k,v in hmap.items():
            if v == maxGr:
                res+=1
        return res
    def digSum(self, dig):
        res = 0
        for i in str(dig):
            res+=int(i)
        return res