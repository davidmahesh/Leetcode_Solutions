class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        return [i for i, x in enumerate(nums) if x == target]
