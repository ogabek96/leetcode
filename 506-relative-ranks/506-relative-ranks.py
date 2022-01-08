class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scoresort = sorted(score, reverse = True)
        cnt = 1
        hmap = {}
        for s in scoresort:
            hmap[s] = str(cnt)
            cnt+=1
        for i in range(len(score)):
            if score[i] in hmap.keys():
                score[i] = hmap[score[i]]
        for i in range(len(score)):
            if score[i] == "1":
                score[i] = "Gold Medal"
            if score[i] == "2":
                score[i] = "Silver Medal"
            if score[i] == "3":
                score[i] = "Bronze Medal"
        return score