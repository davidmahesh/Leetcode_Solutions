class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        res = 0
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                res = max(res, j)
                break
        for i in range(n):
            if colors[i] != colors[n - 1]:
                res = max(res, n - 1 - i)
                break
        return res