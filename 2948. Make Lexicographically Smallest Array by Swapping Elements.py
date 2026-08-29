class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        arr = sorted((x, i) for i, x in enumerate(nums))
        ans = [0] * n

        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            indices = sorted(arr[i][1] for i in range(start, end + 1))

            for j, idx in enumerate(indices):
                ans[idx] = arr[start + j][0]

            start = end + 1

        return ans