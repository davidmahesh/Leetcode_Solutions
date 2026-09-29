class Solution:
    def numSpecial(self, mat):
        m = len(mat)
        n = len(mat[0])
        
        row = [sum(r) for r in mat]
        col = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ans += 1
        
        return ans