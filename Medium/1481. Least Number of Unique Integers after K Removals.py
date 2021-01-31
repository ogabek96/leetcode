class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hmap = {}
        for n in arr:
            if n not in hmap:
                hmap[n] = 1
            else:
                hmap[n]+=1
        elms = sorted(hmap.keys(), key=lambda x: hmap[x])
        for i in range(len(elms)):
            k-=hmap[elms[i]]
            if k == 0:
                return len(elms) - (i + 1)
            elif k < 0:
                return len(elms) - i