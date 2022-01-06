class Solution:
    def checkString(self, s: str) -> bool:
        if (len(s) == 1):
            return True
        if 'b' not in s:
            return True
        bind = s.index('b')
        return not 'a' in s[bind:]