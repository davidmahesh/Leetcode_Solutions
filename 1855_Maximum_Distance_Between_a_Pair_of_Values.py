class Solution:
    def maxDistance(self, nums1, nums2):
        i, j = 0, 0
        res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1
                if j < i:
                    j = i
        return res