class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        m = n // 2

        lq = num[:m].count('?')
        rq = num[m:].count('?')

        ls = sum(int(c) for c in num[:m] if c != '?')
        rs = sum(int(c) for c in num[m:] if c != '?')

        if lq == rq:
            return ls != rs

        if (lq - rq) % 2 != 0:
            return True

        if lq > rq:
            return ls - rs + 9 * ((lq - rq) // 2) != 0

        return ls - rs - 9 * ((rq - lq) // 2) != 0