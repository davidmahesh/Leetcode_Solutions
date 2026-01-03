class Solution:
    def numOfWays(self, n):
        mod = 10**9 + 7
        a = 6
        b = 6

        for _ in range(2, n + 1):
            na = (a * 2 + b * 2) % mod
            nb = (a * 2 + b * 3) % mod
            a, b = na, nb

        return (a + b) % mod
