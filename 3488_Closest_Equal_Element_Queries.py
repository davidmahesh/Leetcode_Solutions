class Solution:
    def solveQueries(self, nums, queries):
        from collections import defaultdict
        n = len(nums)
        idx_map = defaultdict(list)
        for i, v in enumerate(nums):
            idx_map[v].append(i)
        import bisect
        def min_circ_dist(positions, q):
            if len(positions) == 1:
                return -1
            pos = bisect.bisect_left(positions, q)
            best = float('inf')
            for p in [pos - 1, pos, pos + 1]:
                j = positions[p % len(positions)]
                if j != q:
                    d = abs(j - q)
                    best = min(best, d, n - d)
            return best
        return [min_circ_dist(idx_map[nums[q]], q) for q in queries]