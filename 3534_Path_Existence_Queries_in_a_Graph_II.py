from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        a = [0] * n
        for i, v in enumerate(order):
            pos[v] = i
            a[i] = nums[v]

        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and a[j + 1] - a[i] <= maxDiff:
                j += 1
            nxt[i] = j

        lg = n.bit_length()
        up = [nxt]
        for _ in range(1, lg):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []
        for u, v in queries:
            l = pos[u]
            r = pos[v]
            if l > r:
                l, r = r, l
            if l == r:
                ans.append(0)
                continue
            if nxt[l] == l:
                ans.append(-1)
                continue
            cur = l
            steps = 0
            for b in range(lg - 1, -1, -1):
                x = up[b][cur]
                if x < r:
                    cur = x
                    steps += 1 << b
            if nxt[cur] < r:
                ans.append(-1)
            else:
                ans.append(steps + 1)
        return ans