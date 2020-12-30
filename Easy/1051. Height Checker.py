class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hSorted = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if hSorted[i] != heights[i]:
                cnt+=1
        return cnt