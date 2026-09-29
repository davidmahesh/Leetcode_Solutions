class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        diff = [0] * (2*limit+2)

        for i in range(n//2):
            a, b = nums[i], nums[n-1-i]
            lo, hi = min(a,b), max(a,b)
            diff[lo+1]    -= 1
            diff[hi+limit+1] += 1
            diff[a+b]     -= 1
            diff[a+b+1]   += 1

        res = n
        cur = n
        for t in range(2, 2*limit+1):
            cur += diff[t]
            res = min(res, cur)
        return res