class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        NEG = float('-inf')
        dp = [[[NEG]*(k+1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                sc = v
                co = 0 if v == 0 else 1
                for c in range(k+1):
                    best = NEG
                    if i == 0 and j == 0:
                        best = 0
                    if i > 0 and dp[i-1][j][c] != NEG:
                        best = max(best, dp[i-1][j][c])
                    if j > 0 and dp[i][j-1][c] != NEG:
                        best = max(best, dp[i][j-1][c])
                    if best == NEG:
                        continue
                    nc = c + co
                    if nc <= k:
                        dp[i][j][nc] = max(dp[i][j][nc], best + sc)
        ans = max(dp[m-1][n-1])
        return ans if ans != NEG else -1