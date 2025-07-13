class Solution:
    def rotateMatrix(self, mat):
        n = len(mat)
        
        res = [[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                res[n - 1 - j][i] = mat[i][j]
        
        for i in range(n):
            for j in range(n):
                mat[i][j] = res[i][j]

        return mat