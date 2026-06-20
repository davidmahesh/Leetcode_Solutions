from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        res = sorted(restrictions)
        res = [[1, 0]] + res + [[n, n-1]]

        m = len(res)
        for i in range(1, m):
            res[i][1] = min(res[i][1], res[i-1][1] + (res[i][0] - res[i-1][0]))
        for i in range(m-2, -1, -1):
            res[i][1] = min(res[i][1], res[i+1][1] + (res[i+1][0] - res[i][0]))

        best = 0
        for i in range(1, m):
            id1, h1 = res[i-1]
            id2, h2 = res[i]
            dist = id2 - id1
            peak = (h1 + h2 + dist) // 2
            best = max(best, peak)

        return best