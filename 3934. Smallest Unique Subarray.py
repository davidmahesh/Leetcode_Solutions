import random

class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        m1 = 1000000007
        m2 = 1000000009
        b1 = random.randint(100007, 500000000)
        b2 = random.randint(100007, 500000000)

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i, x in enumerate(nums):
            p1[i + 1] = (p1[i] * b1) % m1
            p2[i + 1] = (p2[i] * b2) % m2
            h1[i + 1] = (h1[i] * b1 + x) % m1
            h2[i + 1] = (h2[i] * b2 + x) % m2

        def ok(k):
            seen = set()
            dup = set()
            pk1 = p1[k]
            pk2 = p2[k]
            for a1, c1, a2, c2 in zip(h1, h1[k:], h2, h2[k:]):
                val = (((c1 - a1 * pk1) % m1) << 32) | ((c2 - a2 * pk2) % m2)
                if val in seen:
                    dup.add(val)
                else:
                    seen.add(val)
            return len(seen) > len(dup)

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
