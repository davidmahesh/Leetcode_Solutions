class Solution:
    def maxProductPath(self, grid):
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        mx = [[0]*n for _ in range(m)]
        mn = [[0]*n for _ in range(m)]
        
        mx[0][0] = mn[0][0] = grid[0][0]
        
        for i in range(1, m):
            mx[i][0] = mn[i][0] = mx[i-1][0] * grid[i][0]
        for j in range(1, n):
            mx[0][j] = mn[0][j] = mx[0][j-1] * grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                candidates = [mx[i-1][j]*v, mn[i-1][j]*v, mx[i][j-1]*v, mn[i][j-1]*v]
                mx[i][j] = max(candidates)
                mn[i][j] = min(candidates)
        
        if mx[m-1][n-1] < 0:
            return -1
        return mx[m-1][n-1] % mod