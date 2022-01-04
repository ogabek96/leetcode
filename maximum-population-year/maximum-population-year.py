class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs = sorted(logs, key = lambda x: x[0])
        mcnt = 0
        myear = 2051
        for year, _ in logs:
            cnt = 0
            for birth, death in logs:
                if birth <= year and death > year:
                    cnt+=1
            if cnt > mcnt:
                mcnt = cnt
                myear = year
        return myear