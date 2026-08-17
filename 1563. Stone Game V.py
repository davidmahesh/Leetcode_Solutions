from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            maxL[i][i] = pref[i + 1]
            maxR[i][i] = -pref[i]
            mid = i
            for j in range(i + 1, n):
                while mid + 1 < j and 2 * pref[mid + 2] <= pref[j + 1] + pref[i]:
                    mid += 1
                total = pref[j + 1] + pref[i]
                if 2 * pref[mid + 1] > total:
                    val = pref[j + 1] + maxR[i + 1][j]
                elif 2 * pref[mid + 1] == total:
                    cand1 = maxL[i][mid - 1] - pref[i] if mid > i else 0
                    cand2 = (pref[mid + 1] - pref[i]) + max(dp[i][mid], dp[mid + 1][j])
                    cand3 = pref[j + 1] + maxR[mid + 2][j] if mid + 2 <= j else 0
                    val = max(cand1, cand2, cand3)
                else:
                    cand1 = maxL[i][mid] - pref[i]
                    cand2 = pref[j + 1] + maxR[mid + 2][j] if mid + 2 <= j else 0
                    val = max(cand1, cand2)
                dp[i][j] = val
                maxL[i][j] = max(maxL[i][j - 1], pref[j + 1] + val)
                maxR[i][j] = max(maxR[i + 1][j], val - pref[i])
        return dp[0][n - 1]