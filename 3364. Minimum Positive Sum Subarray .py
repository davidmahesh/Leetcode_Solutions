class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            total = 0
            for j in range(i, min(n, i + r)):
                total += nums[j]

                if j - i + 1 >= l and total > 0:
                    ans = min(ans, total)

        return ans if ans != float('inf') else -1
