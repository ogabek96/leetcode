class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        while num > 1:
            found = False
            for n in (2, 3, 5):
                if num % n == 0:
                    num = num / n
                    found = True
                    if num == 1:
                        return True
            if not found:
                return False
        return False