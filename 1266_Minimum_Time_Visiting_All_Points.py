class Solution:
    def minTimeToVisitAllPoints(self, points):
        ans = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            ans += max(abs(x2 - x1), abs(y2 - y1))
        return ans
