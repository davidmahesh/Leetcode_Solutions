from bisect import bisect_left

class Solution:
    def maxDistance(self, side, points, k):
        def perim(x, y):
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 2*side + (side - x)
            return 3*side + (side - y)
        pos = sorted(perim(x, y) for x, y in points)
        n = len(pos)
        total = 4 * side
        ext = pos + [p + total for p in pos]

        def check(d):
            for s in range(n):
                j = s
                cur = ext[s]
                ok = True
                for _ in range(k - 1):
                    nj = bisect_left(ext, cur + d, j + 1, s + n)
                    if nj >= s + n:
                        ok = False
                        break
                    j = nj
                    cur = ext[j]
                if ok and ext[s] + total - cur >= d:
                    return True
            return False
        lo, hi = 1, 2 * side
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans