class Solution:
    def countSubmatrices(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        count = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1])
                if prefix[i][j] <= k:
                    count += 1
        
        return count