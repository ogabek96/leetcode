class Solution:
    def countPoints(self, rings: str) -> int:
        hmap = defaultdict(list)
        cnt = 0
        for i in range(len(rings) - 1):
            col = rings[i]
            rod = rings[i + 1]
            hmap[rod].append(col)
        for rod, colors in hmap.items():
            if 'R' in colors and 'G' in colors and 'B' in colors:
                cnt+=1
        return cnt