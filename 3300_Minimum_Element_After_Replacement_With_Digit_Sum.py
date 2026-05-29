class Solution:
    def minElement(self, nums):
        return min(sum(int(d) for d in str(n)) for n in nums)