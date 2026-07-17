from bisect import bisect_left
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        freq = [0] * (m + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (m + 1)
        for g in range(1, m + 1):
            s = 0
            for j in range(g, m + 1, g):
                s += freq[j]
            cnt[g] = s * (s - 1) // 2

        exact = [0] * (m + 1)
        for g in range(m, 0, -1):
            exact[g] = cnt[g]
            for j in range(g * 2, m + 1, g):
                exact[g] -= exact[j]

        pref = []
        vals = []
        cur = 0
        for g in range(1, m + 1):
            if exact[g]:
                cur += exact[g]
                pref.append(cur)
                vals.append(g)

        ans = []
        for q in queries:
            ans.append(vals[bisect_left(pref, q + 1)])
        return ans