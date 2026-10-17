class Solution:
    def minSwaps(self, nums):
        def digit_sum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {x: i for i, x in enumerate(nums)}
        ans = 0

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                j = pos[arr[i]]
                pos[nums[i]] = j
                pos[arr[i]] = i
                nums[i], nums[j] = nums[j], nums[i]
                ans += 1

        return ans
