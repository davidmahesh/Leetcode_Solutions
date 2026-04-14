class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        expanded = []
        for pos, limit in factory:
            for _ in range(limit):
                expanded.append(pos)
        n, m = len(robot), len(expanded)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[n] = 0
        for j in range(m - 1, -1, -1):
            new_dp = dp[:]
            for i in range(n - 1, -1, -1):
                if dp[i + 1] != INF:
                    new_dp[i] = min(abs(robot[i] - expanded[j]) + dp[i + 1], new_dp[i])
            dp = new_dp
        return dp[0]