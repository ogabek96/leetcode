class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        binary = ""
        while N >= 1:
            binary = str(N % 2) + binary
            N = int(N / 2)
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