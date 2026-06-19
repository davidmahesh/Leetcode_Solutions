class Solution:
    def largestAltitude(self, gain):
        cur = 0
        best = 0
        for g in gain:
            cur += g
            best = max(best, cur)
        return best