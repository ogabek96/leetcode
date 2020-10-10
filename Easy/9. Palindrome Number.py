class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        leng = len(x)
        for i in range(leng):
            if x[i] != x[leng - 1 - i] :
                return False
        return True