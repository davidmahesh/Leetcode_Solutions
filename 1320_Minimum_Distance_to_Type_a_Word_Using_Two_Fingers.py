class Solution:
    def minimumDistance(self, word):
        def dist(a, b):
            if a == 26:
                return 0
            return abs(a//6 - b//6) + abs(a%6 - b%6)
        n = len(word)
        w = [ord(c) - ord('A') for c in word]
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(i, f1, f2):
            if i == n:
                return 0
            c = w[i]
            return min(
                dist(f1, c) + dp(i+1, c, f2),
                dist(f2, c) + dp(i+1, f1, c)
            )
        return dp(0, 26, 26)