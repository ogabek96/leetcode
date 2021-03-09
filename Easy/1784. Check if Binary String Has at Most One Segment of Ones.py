class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        lastOne = -1
        for i in range(len(s)):
            if s[i] == '1':
                if lastOne != -1:
                    if i - lastOne != 1:
                        return False
                    lastOne = i
                else:
                    lastOne = i
        return True