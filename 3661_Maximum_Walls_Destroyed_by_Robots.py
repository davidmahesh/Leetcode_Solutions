from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots, distance, walls):
        n = len(robots)
        order = sorted(range(n), key=lambda i: robots[i])
        pos = [robots[order[i]] for i in range(n)]
        dist = [distance[order[i]] for i in range(n)]
        sw = sorted(walls)
        def count(lo, hi):
            if lo > hi:
                return 0
            return bisect_right(sw, hi) - bisect_left(sw, lo)
        at0 = count(pos[0], pos[0])
        dp = [at0 + count(pos[0] - dist[0], pos[0] - 1), at0]
        for i in range(n - 1):
            rr = count(pos[i] + 1, min(pos[i] + dist[i], pos[i+1] - 1))
            ll = count(max(pos[i+1] - dist[i+1], pos[i] + 1), pos[i+1] - 1)
            ov = count(max(pos[i+1] - dist[i+1], pos[i] + 1), min(pos[i] + dist[i], pos[i+1] - 1))
            at_next = count(pos[i+1], pos[i+1])
            new0 = at_next + max(dp[0] + ll, dp[1] + rr + ll - ov)
            new1 = at_next + max(dp[0], dp[1] + rr)
            dp = [new0, new1]
        return max(dp[0], dp[1] + count(pos[n-1] + 1, pos[n-1] + dist[n-1]))