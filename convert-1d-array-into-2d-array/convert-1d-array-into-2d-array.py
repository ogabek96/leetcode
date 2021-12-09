class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        mat = [[0 for i in range(n)] for j in range(m)]
        cnt = 0
        if len(original) != m * n:
            return []
        for i in range(m):
            for j in range(n):
                print(i, j)
                mat[i][j] = original[cnt]
                cnt+=1
        return mat