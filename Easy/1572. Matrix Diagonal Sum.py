class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        prim = 0
        sec = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i == j:
                    prim+=mat[i][i]
                if i + j == n - 1:
                    sec+=mat[i][j]
        res = prim + sec
        if n % 2 == 1:
           res-= mat[n//2][n//2]
        return res