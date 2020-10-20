class Solution:
    newStr = ''
    def isPalindrome(self, s: str) -> bool:
        for ss in s:
            if ord(ss.lower()) >= 97 and ord(ss.lower()) <= 122 or (ord(ss.lower()) >= 48 and ord(ss.lower()) <= 57):
                self.newStr += ss.lower()
        leng = len(self.newStr)
        for i in range(leng):
            if self.newStr[i] != self.newStr[leng - i - 1]:
                return False
        return True