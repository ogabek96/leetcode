class Solution:
    def equalFrequency(self, word: str) -> bool:
        hmap = {}
        for ch in word:
            hmap[ch] = hmap.get(ch, 0) + 1
        if len(hmap.values()) == 1:
            return True
        freqs = sorted(hmap.values())
        freqs[-1]-=1
        op1 = True
        op2 = True
        for f in freqs:
            if freqs[0] != f:
                op1 = False
                break
        freqs[-1]+=1
        freqs[0]-=1
        for f in freqs:
            if f != 0 and freqs[1] != f:
                op2 = False
                break
        return op1 or op2