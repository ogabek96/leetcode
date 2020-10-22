class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        def comp(a):
            return a[1] - a[0]
        costs = sorted(costs, key=comp, reverse=True)
        n = len(costs)
        for i in range(int(n/2)):
            res+=costs[i][0]
            res+=costs[int(n/2) + i][1]
        return res