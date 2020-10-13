class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a = {}
        for p in paths:
            a[p[0]] = p[1]
        for p in paths:
            if a.get(p[1]) == None:
                return p[1]