class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hmap = {}
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        for n in deck:
            hmap[n] = hmap.get(n, 0) + 1
        values = list(hmap.values())
        res = values[0]
        for n in values[1:]:
            res = gcd(res, n)
        
        return res >= 2