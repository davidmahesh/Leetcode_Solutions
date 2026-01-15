class Solution:
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        hBars.sort()
        vBars.sort()

        def longest(bars):
            best = cur = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    cur += 1
                else:
                    best = max(best, cur)
                    cur = 1
            best = max(best, cur)
            return best + 1

        h = longest(hBars)
        v = longest(vBars)

        s = min(h, v)
        return s * s
