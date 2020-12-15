class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        partSum = sum(A)
        if partSum % 3 != 0:
            return False
        partSum/=3
        sumSoFar = 0
        cnt = 0
        for n in A:
            if cnt == 2 and sum(A) - partSum * 2 == partSum:
                return True
            sumSoFar+=n
            if sumSoFar == partSum:
                cnt+=1
                sumSoFar = 0
