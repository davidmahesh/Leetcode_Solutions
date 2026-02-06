class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        ans = n
        l = 0

        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            curr = r - l + 1
            rem = n - curr
            if rem < ans:
                ans = rem

        return ans
