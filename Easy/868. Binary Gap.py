class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        dist = 0
        s = 0
        for i in range(len(b)):
            if b[i] == '1':
                dist = max(dist, i - s)
                s = i
        return dist