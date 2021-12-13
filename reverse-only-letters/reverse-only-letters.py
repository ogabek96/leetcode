class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        english = []
        letters = list(s)
        for ch in letters:
            if ch.lower() >= 'a' and ch.lower() <= 'z':
                english.append(ch)
        cnt = len(english) - 1
        for i in range(len(letters)):
            if letters[i].lower() >= 'a' and letters[i].lower() <= 'z':
                letters[i] = english[cnt]
                cnt-=1
        return "".join(letters)