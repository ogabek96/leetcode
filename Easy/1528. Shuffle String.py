class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = [0]*len(s)
        res = ''
        for i in range(len(s)):
            temp[indices[i]] = s[i]
        for t in temp:
            res+=t
        return res