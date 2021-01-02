class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = {}
        for ch in s:
            if ch in hmap:
                hmap[ch]+=1
            else:
                hmap[ch] = 1
        s = sorted(s, reverse = True)
        return sorted(s, key=lambda x: hmap[x], reverse=True)