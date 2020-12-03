class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        andy = {}
        doris = {}
        for i in range(len(list1)):
            andy[list1[i]] = i
        for i in range(len(list2)):
            doris[list2[i]] = i
        ans = []
        for i in range(len(list1)):
            el1 = list1[i]
            if el1 in andy and el1 in doris:
                ans.append((andy[el1], doris[el1]))
        res = []
        ans = sorted(ans, key=lambda x: x[0] + x[1])
        for i in range(len(ans)):
            if ans[i][0] + ans[i][1] == ans[0][0] + ans[0][1]:
                res.append(list1[ans[i][0]])
        return res