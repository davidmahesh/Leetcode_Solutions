class Solution:
    def maxSideLength(self, mat, threshold):
        m = len(mat)
        n = len(mat[0])

        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + mat[i][j]

        def ok(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    s = ps[i][j] - ps[i - k][j] - ps[i][j - k] + ps[i - k][j - k]
                    if s <= threshold:
                        return True
            return False

        l, r = 0, min(m, n)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
