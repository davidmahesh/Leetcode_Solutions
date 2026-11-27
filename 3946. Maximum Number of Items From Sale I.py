class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        free = []

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    count += 1
            free.append(count + 1)

        groups = {}
        for i in range(n):
            f, p = items[i]
            groups.setdefault(p, []).append(free[i])

        dp = [-10**9] * (budget + 1)
        dp[0] = 0
        ans = 0

        for p in sorted(groups, reverse=True):
            cur = [-10**9] * (budget + 1)

            for val in groups[p]:
                for j in range(budget, p - 1, -1):
                    cur[j] = max(
                        cur[j],
                        dp[j - p] + val,
                        cur[j - p] + val
                    )

            for j in range(budget + 1):
                if cur[j] >= 0:
                    ans = max(ans, cur[j] + (budget - j) // p)

            for val in groups[p]:
                for j in range(budget, p - 1, -1):
                    dp[j] = max(dp[j], dp[j - p] + val)

        return ans
