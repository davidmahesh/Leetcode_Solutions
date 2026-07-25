class Solution:
    def maxProduct(self, n: int) -> int:
        a = []
        while n:
            a.append(n % 10)
            n //= 10

        ans = 0
        m = len(a)
        for i in range(m):
            for j in range(i + 1, m):
                ans = max(ans, a[i] * a[j])

        return ans