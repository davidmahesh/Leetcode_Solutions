class Solution:
    def separateDigits(self, nums):
        return [int(d) for n in nums for d in str(n)]