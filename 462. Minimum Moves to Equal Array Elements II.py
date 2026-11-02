class Solution:
    def minMoves2(self, nums):
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(x - mid) for x in nums)
