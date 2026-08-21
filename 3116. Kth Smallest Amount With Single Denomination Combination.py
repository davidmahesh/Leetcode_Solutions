from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0

            for mask in range(1, 1 << n):
                v = 1
                bits = 0
                ok = True

                for i in range(n):
                    if mask & (1 << i):
                        v = lcm(v, coins[i])
                        if v > x:
                            ok = False
                            break
                        bits += 1

                if ok:
                    cur = x // v
                    if bits & 1:
                        ans += cur
                    else:
                        ans -= cur

            return ans

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo