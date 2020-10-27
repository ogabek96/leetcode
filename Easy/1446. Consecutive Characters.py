class Solution:
    def maxPower(self, s: str) -> int:
        maxLen = 1
        maxSoFar = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                maxLen+=1
            else:
                maxLen = 1
            if maxLen > maxSoFar:
                maxSoFar = maxLen
        return maxSoFar
                