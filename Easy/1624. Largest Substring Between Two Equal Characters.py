class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hmap = {}
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = [i, i]
            else:
                a, b = hmap[s[i]]
                hmap[s[i]] = [a, i]
        if(len(hmap.items()) == 0):
            return -1
        maxA, maxB = 0, 0
        for k, v in hmap.items():
            a, b = v
            if (b - a) > (maxB - maxA):
                maxA = a
                maxB = b
        return maxB - maxA - 1