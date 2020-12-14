class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        cnt = 0
        for b in bills:
            if b == 5:
                five+=1
            elif b == 10:
                if five == 0:
                    return False
                five-=1
                ten+=1
            elif b == 20:
                q = 15
                if ten > 0:
                    q-=10
                    ten-=1
                if five * 5 >= q:
                    five-= q / 5
                    q = 0
                if q > 0:
                    return False
                cnt+=1
        return True