class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = sorted([abs(a - b) for a, b in zip(nums1, nums2)], reverse=True)
        k = k1 + k2
        n = len(diff)

        if sum(diff) <= k:
            return 0

        diff.append(0)

        for i in range(n):
            need = (diff[i] - diff[i + 1]) * (i + 1)
            if k >= need:
                k -= need
            else:
                q, r = divmod(k, i + 1)
                level = diff[i] - q
                return (
                    sum(x * x for x in diff[i + 1:n])
                    + r * (level - 1) ** 2
                    + (i + 1 - r) * level ** 2
                )

        return 0
