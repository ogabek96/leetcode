class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = True
        dec = True
        first = A[0]
        for n in A:
            if not n >= first:
                inc = False
            if not n <= first:
                dec = False
            first = n
        return inc or dec