class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {}
        for n in arr:
            if n in hmap:
                hmap[n]+= 1
            else:
                hmap[n] = 1
        keys = sorted(hmap.values())
        for i in range(len(keys) - 1):
            if keys[i] == keys[i + 1]:
                return False
        return True
        