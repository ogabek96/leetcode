class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        words = s.split(" ")
        for i in range(len(words)):
            res.append(self.reverse(words[i]))
        return " ".join(res)
    def reverse(self, s1: str):
        res = ""
        for i in range(len(s1)-1, -1, -1):
            res+= s1[i]
        return res