from typing import List

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_POS = 50001
        N = 1
        while N < MAX_POS:
            N <<= 1

        mg = [0] * (2*N)
        lf = [10**9] * (2*N)
        rl = [0] * (2*N)
        ho = [False] * (2*N)

        def _merge(v):
            L, R = 2*v, 2*v+1
            ho[v] = ho[L] or ho[R]
            lf[v] = lf[L] if ho[L] else lf[R]
            rl[v] = rl[R] if ho[R] else rl[L]
            m = mg[L] if mg[L] > mg[R] else mg[R]
            if ho[L] and ho[R]:
                g = lf[R] - rl[L]
                if g > m: m = g
            mg[v] = m

        def update(pos):
            i = pos + N
            ho[i] = True
            lf[i] = rl[i] = pos
            mg[i] = 0
            i >>= 1
            while i:
                _merge(i)
                i >>= 1

        def query(ql, qr):
            l, r = ql + N, qr + N
            lp, rp = [], []
            while l <= r:
                if l & 1: lp.append(l); l += 1
                if not r & 1: rp.append(r); r -= 1
                l >>= 1; r >>= 1
            rmg, rlf, rrl, rho = 0, 0, 0, False
            for seg in lp + rp[::-1]:
                if not ho[seg]: continue
                if not rho:
                    rmg, rlf, rrl, rho = mg[seg], lf[seg], rl[seg], True
                else:
                    g = lf[seg] - rrl
                    if g > rmg: rmg = g
                    if mg[seg] > rmg: rmg = mg[seg]
                    rrl = rl[seg]
            return rmg, rlf, rrl, rho

        results = []
        for q in queries:
            if q[0] == 1:
                update(q[1])
            else:
                x, sz = q[1], q[2]
                qmg, qlf, qrl, qho = query(0, x)
                if not qho:
                    results.append(x >= sz)
                else:
                    ma = max(qlf, x - qrl, qmg)
                    results.append(ma >= sz)
        return results