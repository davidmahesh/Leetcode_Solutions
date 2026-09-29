class Solution:
    def isGood(self, nums):
        n = max(nums)
        if len(nums) != n+1:
            return False
        from collections import Counter
        c = Counter(nums)
        for i in range(1, n):
            if c[i] != 1:
                return False
        return c[n] == 2