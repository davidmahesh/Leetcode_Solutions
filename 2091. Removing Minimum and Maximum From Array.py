    class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        if n == 1:
            return 1

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        a = min(mn, mx)
        b = max(mn, mx)

        front = b + 1
        back = n - a
        both = (a + 1) + (n - b)

        return min(front, back, both)