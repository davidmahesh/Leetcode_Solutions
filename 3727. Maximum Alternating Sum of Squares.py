class Solution:
    def maxAlternatingSum(self, nums):
        nums = sorted((x * x for x in nums), reverse=True)
        mid = (len(nums) + 1) // 2
        
        return sum(nums[:mid]) - sum(nums[mid:])
