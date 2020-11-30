class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        colLen = len(A[0])
        rowLen = len(A)
        for i in range(colLen):
            temp = []
            for j in range(rowLen):
                temp.append(A[j][i])
            B.append(temp)
        return B
            