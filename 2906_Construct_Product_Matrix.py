class Solution:
    def constructProductMatrix(self, grid):
        mod = 12345
        n, m = len(grid), len(grid[0])
        total = n * m
        
        flat = [grid[i][j] for i in range(n) for j in range(m)]
        
        pre = [1] * total
        for i in range(1, total):
            pre[i] = pre[i-1] * flat[i-1] % mod
        
        suf = [1] * total
        for i in range(total-2, -1, -1):
            suf[i] = suf[i+1] * flat[i+1] % mod
        
        res = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(pre[idx] * suf[idx] % mod)
                idx += 1
            res.append(row)
        
        return res