class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCan = max(candies)
        res = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] < maxCan and candies[i] + extraCandies >= maxCan:
                res[i] = True
            elif candies[i] == maxCan:
                res[i] = True
        return res