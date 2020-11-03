class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        strVowels = []
        for ch in s:
            if ch in vowels:
                strVowels.append(ch)
        newStr = ""
        for ch in s:
            if ch in vowels:
                newStr+=strVowels.pop(-1)
            else:
                newStr+=ch
        return newStr