class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        while num >= 1:
            binary = str(num % 2) + binary
            num = int(num / 2)
        complement = ""
        for n in binary:
            if n == "1":
                complement+="0"
            else:
                complement+="1"
        res = 0
        cnt = len(complement) - 1
        for n in complement:
            res+=2**cnt*int(n)
            cnt-=1
        return res