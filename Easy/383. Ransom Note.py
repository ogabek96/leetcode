class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = [0]*256
        for m in magazine:
            chars[ord(m)]+=1
        
        for r in ransomNote:
            if chars[ord(r)] == 0:
                return False
            else:
                chars[ord(r)]-=1
        return True
        