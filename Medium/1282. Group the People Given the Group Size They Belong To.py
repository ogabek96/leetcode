class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mem = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in mem:
                mem[groupSizes[i]] = [i]
            else:
                mem[groupSizes[i]].append(i)
        res = []
        for k,v in mem.items():
            if len(v) <= k:
                res.append(v)
            else:
                res+=(self.split(v, k))
        return res
    def split(self, arr, n):
        res = []
        for i in range(0, len(arr), n):
            res.append(arr[i:i+n])
        return res