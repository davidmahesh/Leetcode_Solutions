class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        if (m + n - 1) % 2:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cur = dp[i][j]
                change = 1 if grid[i][j] == '(' else -1

                if i > 0:
                    for balance in dp[i - 1][j]:
                        if balance + change >= 0:
                            cur.add(balance + change)

                if j > 0:
                    for balance in dp[i][j - 1]:
                        if balance + change >= 0:
                            cur.add(balance + change)

        return 0 in dp[m - 1][n - 1]
