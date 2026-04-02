class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == NEG_INF:
                        continue
                    for ni, nj in [(i+1, j), (i, j+1)]:
                        if ni < m and nj < n:
                            v = coins[ni][nj]
                            dp[ni][nj][k] = max(dp[ni][nj][k], dp[i][j][k] + v)
                            if v < 0 and k < 2:
                                dp[ni][nj][k+1] = max(dp[ni][nj][k+1], dp[i][j][k])
        return max(dp[m-1][n-1])