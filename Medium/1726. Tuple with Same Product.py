class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hmap = {}
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                p = nums[i] * nums[j]
                if p in hmap:
                    hmap[p]+=1
                else:
                    hmap[p] = 1
                res+= (hmap[p] - 1) * 8
        return res