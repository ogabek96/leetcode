class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len1 = len(s)
        str1 = [None] * 255
        str2 = [None] * 255
        for i in range(len1):
            if str1[ord(s[i])] == None:
                str1[ord(s[i])] = i
            if str2[ord(t[i])] == None:
                str2[ord(t[i])] = i
        for i in range(len1):
            if str1[ord(s[i])] != str2[ord(t[i])]:
                return False
        return True