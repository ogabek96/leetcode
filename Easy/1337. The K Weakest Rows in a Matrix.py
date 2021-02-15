class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hmap = {}
        for i in range(len(mat)):
            for n in mat[i]:
                if n == 1:
                    hmap[i] = hmap.get(i, 0) + 1
                else:
                    hmap[i] = hmap.get(i, 0)
        res = list(hmap.keys())
        res = sorted(res, key=lambda x: hmap[x])
        return res[:k]