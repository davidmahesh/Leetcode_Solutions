class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k

        for x in nums:
            r = x % k
            ndp = [0] * k
            ndp[r] += 1

            for p in range(k):
                if dp[p]:
                    ndp[(p * r) % k] += dp[p]

            dp = ndp

            for r in range(k):
                ans[r] += dp[r]

        return ans
