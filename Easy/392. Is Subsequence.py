class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for ch in reversed(t):
            if len(s) == 0:
                return True
            if ch == s[-1]:
                s = s[:-1]
        return len(s) == 0