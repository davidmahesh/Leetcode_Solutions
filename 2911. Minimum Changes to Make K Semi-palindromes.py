class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        cost = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        positions = list(range(i + r, j + 1, d))

                        left, right = 0, len(positions) - 1

                        while left < right:
                            if s[positions[left]] != s[positions[right]]:
                                changes += 1
                            left += 1
                            right -= 1

                    cost[i][j] = min(cost[i][j], changes)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for parts in range(1, k + 1):
                for j in range(i + 1, n):
                    if dp[j + 1][parts - 1] != float('inf'):
                        dp[i][parts] = min(
                            dp[i][parts],
                            cost[i][j] + dp[j + 1][parts - 1]
                        )

        return dp[0][k]
