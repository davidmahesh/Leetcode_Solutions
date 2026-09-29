class Solution:
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
        
        best = 0
        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            for j, val in enumerate(row):
                if val == 0:
                    break
                best = max(best, val * (j + 1))
        
        return best