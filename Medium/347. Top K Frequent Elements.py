class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            if n in hmap:
                hmap[n]+=1
            else:
                hmap[n] = 1
        els = sorted(hmap.keys(), reverse=True, key=lambda x: hmap[x])
        return els[:k]