class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        f = sum(i*v for i,v in enumerate(nums))
        res = f
        for k in range(1, n):
            f += total - n * nums[n-k]
            res = max(res, f)
        return res