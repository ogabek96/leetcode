class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)
        hmap = {}
        for num in A:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num]+=1
        for k, v in hmap.items():
            if v == n / 2:
                return k