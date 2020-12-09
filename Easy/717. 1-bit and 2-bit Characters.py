class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        startInd = 0
        cnt = 0
        while cnt < len(bits):
            if cnt == len(bits) - 1:
                return True
            if bits[cnt] == 0 and bits[cnt + 1] == 0:
                startInd = cnt
            if bits[cnt] == 1 and (bits[cnt + 1] == 0 or bits[cnt+1] == 1):
                startInd = cnt
                cnt+=1
            cnt+=1
        return False