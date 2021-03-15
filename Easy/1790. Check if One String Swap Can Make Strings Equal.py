class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        str1 = ""
        str2 = ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                str1+=s1[i]
                str2+=s2[i]
                cnt+=1
        if cnt > 2:
            return False
        return sorted(str1) == sorted(str2)
        