class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        dp = [[0]*m, [0]*m]

        for v in range(m):
            dp[0][v] = v
            dp[1][v] = m-1-v

        for _ in range(n - 2):
            ndp = [[0]*m, [0]*m]
            suf = [0]*(m+1)
            for x in range(m-1, -1, -1):
                suf[x] = (suf[x+1] + dp[0][x]) % MOD
            for y in range(m):
                ndp[1][y] = suf[y+1]

            pre = [0]*(m+1)
            for x in range(m):
                pre[x+1] = (pre[x] + dp[1][x]) % MOD
            for y in range(m):
                ndp[0][y] = pre[y]

            dp = ndp

        return sum(dp[0][v] + dp[1][v] for v in range(m)) % MOD