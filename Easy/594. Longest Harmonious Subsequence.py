class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hmap = {}
        res = 0
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        for k, v in hmap.items():
            if k + 1 in hmap:
                res = max(res, v + hmap[k + 1])
        return res