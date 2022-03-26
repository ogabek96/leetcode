class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hmap = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    hmap[list1[i]] = i + j
        result = []
        minv = min(hmap.values())
        for k, v in hmap.items():
            if v == minv:
                result.append(k)
        return result