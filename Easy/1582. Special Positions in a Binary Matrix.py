class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        sumRow= [0] * len(mat)
        sumCol= [0] * len(mat[0])
        res = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                sumRow[i]+=mat[i][j]
                sumCol[j]+=mat[i][j]                 
        
        print(sumCol, sumRow)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if sumRow[i] + sumCol[j] == 2 and 1 == mat[i][j]:
                    res+=1
        return res