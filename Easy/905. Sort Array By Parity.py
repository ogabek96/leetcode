class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for n in A:
            if n & 1 == 0:
                even.append(n)
            else:
                odd.append(n)
        return even + odd