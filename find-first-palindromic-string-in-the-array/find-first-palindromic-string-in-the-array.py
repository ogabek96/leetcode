class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def ispalind(s):
            for i in range(len(s)):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True
        for word in words:
            if ispalind(word):
                return word
        return ""
