class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hmap = {}
        arrSort = sorted(set(arr.copy()))
        for i in range(len(arrSort)):
            hmap[arrSort[i]] = i + 1
        rank = []
        for i in range(len(arr)):
            rank.append(hmap[arr[i]])
        return rank