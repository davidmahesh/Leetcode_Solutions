class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = 0
        total = 0
        longest = -1

        for right in range(len(nums)):
            total += nums[right]

            while left <= right and total > target:
                total -= nums[left]
                left += 1

            if total == target:
                longest = max(longest, right - left + 1)

        return -1 if longest == -1 else len(nums) - longest
