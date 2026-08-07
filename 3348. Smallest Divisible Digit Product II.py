class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        req2 = req3 = req5 = req7 = 0
        temp = t

        while temp % 2 == 0:
            temp //= 2
            req2 += 1
        while temp % 3 == 0:
            temp //= 3
            req3 += 1
        while temp % 5 == 0:
            temp //= 5
            req5 += 1
        while temp % 7 == 0:
            temp //= 7
            req7 += 1

        if temp > 1:
            return "-1"

        dp = [[float("inf")] * 40 for _ in range(60)]
        dp[0][0] = 0

        trans = [(1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2)]

        for i in range(60):
            for j in range(40):
                if dp[i][j] == float("inf"):
                    continue
                for d2, d3 in trans:
                    ni = min(59, i + d2)
                    nj = min(39, j + d3)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 1)

        for i in range(59, -1, -1):
            for j in range(39, -1, -1):
                if i < 59:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j])
                if j < 39:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1])

        F2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
        F3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
        F5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        F7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        n = len(num)

        has_zero = False
        first_zero = n
        for i, c in enumerate(num):
            if c == "0":
                has_zero = True
                first_zero = i
                break

        if not has_zero:
            r2, r3, r5, r7 = req2, req3, req5, req7
            for c in num:
                d = int(c)
                r2 = max(0, r2 - F2[d])
                r3 = max(0, r3 - F3[d])
                r5 = max(0, r5 - F5[d])
                r7 = max(0, r7 - F7[d])

            if r2 == r3 == r5 == r7 == 0:
                return num

        limit = min(n - 1, first_zero)

        p2 = p3 = p5 = p7 = 0
        for i in range(limit):
            d = int(num[i])
            p2 += F2[d]
            p3 += F3[d]
            p5 += F5[d]
            p7 += F7[d]

        for i in range(limit, -1, -1):
            for d in range(int(num[i]) + 1, 10):
                need2 = max(0, req2 - p2 - F2[d])
                need3 = max(0, req3 - p3 - F3[d])
                need5 = max(0, req5 - p5 - F5[d])
                need7 = max(0, req7 - p7 - F7[d])

                left = n - 1 - i

                if need5 + need7 + dp[need2][need3] <= left:
                    ans = list(num[:i])
                    ans.append(str(d))

                    c2, c3, c5, c7 = need2, need3, need5, need7

                    for pos in range(left):
                        for x in range(1, 10):
                            t2 = max(0, c2 - F2[x])
                            t3 = max(0, c3 - F3[x])
                            t5 = max(0, c5 - F5[x])
                            t7 = max(0, c7 - F7[x])

                            if t5 + t7 + dp[t2][t3] <= left - pos - 1:
                                ans.append(str(x))
                                c2, c3, c5, c7 = t2, t3, t5, t7
                                break

                    return "".join(ans)

            if i > 0:
                d = int(num[i - 1])
                p2 -= F2[d]
                p3 -= F3[d]
                p5 -= F5[d]
                p7 -= F7[d]

        need = req5 + req7 + dp[req2][req3]
        m = max(n + 1, need)

        ans = []

        c2, c3, c5, c7 = req2, req3, req5, req7

        for pos in range(m):
            for x in range(1, 10):
                t2 = max(0, c2 - F2[x])
                t3 = max(0, c3 - F3[x])
                t5 = max(0, c5 - F5[x])
                t7 = max(0, c7 - F7[x])

                if t5 + t7 + dp[t2][t3] <= m - pos - 1:
                    ans.append(str(x))
                    c2, c3, c5, c7 = t2, t3, t5, t7
                    break

        return "".join(ans)