class Solution:
    def reorganizeString(self, S: str) -> str:
        letters = [0] * 256
        for s in S:
            letters[ord(s)] += 1
        res = ""
        last = ""
        for i in range(len(S)):
            maxim = 0
            maxim_j = 0
            for j in range(256):
                if letters[j] >= maxim and chr(j) != last:
                    maxim = letters[j]
                    maxim_j = j
            if maxim == 0:
                return ""
            res+=chr(maxim_j)
            letters[maxim_j]-=1
            last = chr(maxim_j)
        return res