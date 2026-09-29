from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            best = 1
            for x in range(1, d+1):
                j = i+x
                if j >= n or arr[j] >= arr[i]:
                    break
                best = max(best, 1+dp(j))
            for x in range(1, d+1):
                j = i-x
                if j < 0 or arr[j] >= arr[i]:
                    break
                best = max(best, 1+dp(j))
            memo[i] = best
            return best

        return max(dp(i) for i in range(n))