class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            x = 1
            while x * x <= i:
                if not dp[i - x * x]:
                    dp[i] = True
                    break
                x += 1

        return dp[n]