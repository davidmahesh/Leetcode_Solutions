class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        px = [[0] * (n + 1) for _ in range(m + 1)]
        py = [[0] * (n + 1) for _ in range(m + 1)]
        
        count = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x = 1 if grid[i-1][j-1] == 'X' else 0
                y = 1 if grid[i-1][j-1] == 'Y' else 0
                
                px[i][j] = x + px[i-1][j] + px[i][j-1] - px[i-1][j-1]
                py[i][j] = y + py[i-1][j] + py[i][j-1] - py[i-1][j-1]
                
                if px[i][j] == py[i][j] and px[i][j] > 0:
                    count += 1
        
        return count