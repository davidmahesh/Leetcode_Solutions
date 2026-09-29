class Solution:
    def maximumWeight(self, intervals):
        import bisect

        a = sorted((r, l, w, idx) for idx, (l, r, w) in enumerate(intervals))
        n = len(a)
        ends = [x[0] for x in a]

        prev = [bisect.bisect_left(ends, a[i][1]) - 1 for i in range(n)]

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                skip = dp[k][i - 1]

                j = prev[i - 1] + 1
                base = dp[k - 1][j]

                take = (
                    base[0] + a[i - 1][2],
                    tuple(sorted(base[1] + (a[i - 1][3],)))
                )

                if take[0] > skip[0] or (take[0] == skip[0] and take[1] < skip[1]):
                    dp[k][i] = take
                else:
                    dp[k][i] = skip

        ans = (0, ())

        for k in range(1, 5):
            cur = dp[k][n]
            if cur[0] > ans[0] or (cur[0] == ans[0] and cur[1] < ans[1]):
                ans = cur

        return list(ans[1])
