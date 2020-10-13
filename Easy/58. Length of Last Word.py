class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        leng = len(s)
        start = 0
        end = 0
        for i in range(leng):
            if s[i] != ' ':
                start = i
                break
        for i in range(leng):
            if s[leng - i - 1] != ' ':
                end = leng - i - 1
                break
        res = 0
        for i in range(start, end + 1):
            res+=1
            if s[i] == ' ':
                res = 0
        return res