class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        h = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    h[j] += 1
                else:
                    h[j] = 0

            st = []
            for j in range(n + 1):
                cur = h[j] if j < n else 0
                while st and (j == n or h[st[-1]] > cur):
                    ht = h[st.pop()]
                    l = st[-1] + 1 if st else 0
                    ans = max(ans, ht * (j - l))
                st.append(j)

        return ans
