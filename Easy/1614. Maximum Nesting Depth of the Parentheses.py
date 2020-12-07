class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        maxVal = 0
        for ch in s:
            if ch == '(':
                cnt+=1                
            if ch == ')':
                cnt-=1
            maxVal = max(maxVal, cnt)
        return maxVal