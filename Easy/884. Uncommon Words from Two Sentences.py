class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        hmap = {}
        for w in A.split():
            if w not in hmap:
                hmap[w] = 1
            else:
                hmap[w]+=1
        for w in B.split():
            if w not in hmap:
                hmap[w] = 1
            else:
                hmap[w]+=1
        res = []
        for itm in hmap.items():
                if itm[1] == 1:
                    res.append(itm[0])
        return res