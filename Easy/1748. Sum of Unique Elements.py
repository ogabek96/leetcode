class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hmap = {}
        res = 0
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        for k,v in hmap.items():
            if v == 1:
                res+=k
        return res