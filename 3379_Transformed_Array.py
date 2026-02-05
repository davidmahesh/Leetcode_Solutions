class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        res = [0] * n

        for i in range(n):
            if nums[i] == 0:
                res[i] = 0
            else:
                idx = (i + nums[i]) % n
                res[i] = nums[idx]

        return res
