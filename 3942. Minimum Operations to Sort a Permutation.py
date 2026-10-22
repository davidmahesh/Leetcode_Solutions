class Solution:
    def minOperations(self, nums):
        n = len(nums)
        p = nums.index(0)
        ans = float('inf')

        if all(nums[(i + p) % n] == i for i in range(n)):
            ans = min(ans, p, n - p + 2)

        k = n - 1 - p
        if all(nums[(n - 1 - (i + k) % n) % n] == i for i in range(n)):
            ans = min(ans, k + 1, n - k + 1)

        return ans if ans != float('inf') else -1
