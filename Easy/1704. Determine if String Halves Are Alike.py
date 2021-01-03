class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set({'a', 'e', 'i', 'o', 'u'})
        half1 = s[0:len(s) // 2]
        half2 = s[len(s) // 2:]
        vow1 = 0
        vow2 = 0
        for ch in half1:
            if ch.lower() in vowels:
                vow1+=1
        for ch in half2:
            if ch.lower() in vowels:
                vow2+=1
        return vow1 == vow2