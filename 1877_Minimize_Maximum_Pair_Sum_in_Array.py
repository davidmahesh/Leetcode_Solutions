class Solution:
    def minPairSum(self, nums):
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0

        while i < j:
            s = nums[i] + nums[j]
            if s > ans:
                ans = s
            i += 1
            j -= 1

        return ans
