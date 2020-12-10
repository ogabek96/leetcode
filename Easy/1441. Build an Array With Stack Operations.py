class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = []
        cnt = 1
        t = 0
        while cnt <= n and cnt <= target[-1]:
            if target[t] == cnt:
                arr.append("Push")
                cnt+=1
                t+=1
            else:
                arr.append("Push")
                arr.append("Pop")
                cnt+=1
        return arr