class Solution:
    def leftRightDifference(self, nums):
        left = 0
        right = sum(nums)
        res = []
        for n in nums:
            right -= n
            res.append(abs(left - right))
            left += n
        return res