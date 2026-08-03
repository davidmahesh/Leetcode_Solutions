from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            s = 0
            dp[i] = -10 ** 18
            for j in range(i, min(i + 3, n)):
                s += stoneValue[j]
                dp[i] = max(dp[i], s - dp[j + 1])

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"