class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = {}
        for ch in text:
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1
        cnt = 0
        while True:
            if hmap.get('b', 0) < 1:
                return cnt
            hmap['b']-=1
            if hmap.get('a', 0) < 1:
                return cnt
            hmap['a']-=1
            if hmap.get('l', 0) < 2:
                return cnt
            hmap['l']-=2
            if hmap.get('o', 0) < 2:
                return cnt
            hmap['o']-=2
            if hmap.get('n', 0) < 1:
                return cnt
            hmap['n']-=1
            cnt+=1