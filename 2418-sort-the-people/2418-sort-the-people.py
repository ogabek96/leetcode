class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        namesInd = [i for i in range(len(names))]
        namesInd = sorted(namesInd, key = lambda x: heights[x], reverse = True)
        for ind in namesInd:
            res.append(names[ind])
        return res