class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        wmax = int(area ** 0.5)
        wres = 1
        lres = area
        for w in range(1, wmax + 1):
            if area % w == 0:
                l = int(area / w)
                if l - w < 0:
                    break
                if l - w < lres - wres:
                    wres = w
                    lres = l
        return [lres, wres]