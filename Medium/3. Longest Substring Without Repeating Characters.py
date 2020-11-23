class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pA = 0
        pB = 0
        unique = set()
        res = 0
        while pB < len(s):
            if s[pB] not in unique:
                unique.add(s[pB])
                pB+=1
                res = max(res, len(unique))
            else:
                unique.remove(s[pA])
                pA+=1
        return res