class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        leng = len(digits)
        
        for i in range(leng):
            if digits[leng - i - 1] == 9:
                digits[leng - i - 1] = 0
            else:
                digits[leng - i - 1]+=1
                return digits
        return [1, *digits]