class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        mod = 10**9 + 7

        hs = [1] + sorted(hFences) + [m]
        vs = [1] + sorted(vFences) + [n]

        hd = set()
        for i in range(len(hs)):
            for j in range(i + 1, len(hs)):
                hd.add(hs[j] - hs[i])

        best = 0
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                d = vs[j] - vs[i]
                if d in hd:
                    best = max(best, d)

        if best == 0:
            return -1
        return (best * best) % mod
