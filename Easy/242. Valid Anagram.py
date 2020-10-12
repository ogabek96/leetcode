class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1 = len(s)
        len2 = len(t)
        if len1 != len2:
            return False
        
        str1 = [0] * 255
        str2 = [0] * 255
        
        for i in range(len1):
            str1[ord(s[i])] +=1
            str2[ord(t[i])] +=1
        
        for l in s:
            if str1[ord(l)] != str2[ord(l)]:
                return False
        return True