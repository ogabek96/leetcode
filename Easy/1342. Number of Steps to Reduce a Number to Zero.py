class Solution:
    def numberOfSteps (self, num: int) -> int:
        st = 0
        while num > 0:
            if num % 2 == 0:
                num  = num / 2
            else:
                num-=1
            st+=1
        return st