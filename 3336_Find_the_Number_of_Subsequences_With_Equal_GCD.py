from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        mod = 10**9 + 7
        dp = {(0, 0): 1}

        for x in nums:
            ndp = {}
            for (a, b), cnt in dp.items():
                ndp[(a, b)] = (ndp.get((a, b), 0) + cnt) % mod

                na = x if a == 0 else gcd(a, x)
                ndp[(na, b)] = (ndp.get((na, b), 0) + cnt) % mod

                nb = x if b == 0 else gcd(b, x)
                ndp[(a, nb)] = (ndp.get((a, nb), 0) + cnt) % mod
            dp = ndp

        ans = 0
        for (a, b), cnt in dp.items():
            if a == b and a != 0:
                ans = (ans + cnt) % mod
        return ans