class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def canbeformed(digits, num):
            hmap = defaultdict(int)
            for d in digits:
                hmap[d]+=1
            for n in str(num):
                hmap[int(n)] = hmap[int(n)] - 1
                if hmap[int(n)] < 0:
                    return False
            return True
        res = set()
        for i in range(100, 1000, 2):
            if canbeformed(digits, i):
                res.add(i)
        return sorted(res)