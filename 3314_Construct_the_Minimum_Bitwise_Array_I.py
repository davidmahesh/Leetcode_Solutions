class Solution:
    def minBitwiseArray(self, nums):
        res = []
        for x in nums:
            if x & 1 == 0:
                res.append(-1)
                continue
            k = 0
            while ((x >> k) & 1) == 1:
                k += 1
            res.append(x ^ (1 << (k - 1)))
        return res
