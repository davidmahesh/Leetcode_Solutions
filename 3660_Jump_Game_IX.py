class Solution:
    def maxValue(self, nums):
        n = len(nums)
        prefix_max = [0]*n
        suffix_min = [0]*n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        suffix_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
        cuts = []
        for j in range(n-1):
            if prefix_max[j] <= suffix_min[j+1]:
                cuts.append(j)
        cuts.append(n-1)
        ans = [0]*n
        c = 0
        for i in range(n):
            if i > cuts[c]:
                c += 1
            ans[i] = prefix_max[cuts[c]]
        return ans