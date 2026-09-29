class Solution:
    def maximumJumps(self, nums, target):
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for j in range(1, n):
            for i in range(j):
                if dp[i] != -1 and abs(nums[j]-nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i]+1)
        return dp[n-1]