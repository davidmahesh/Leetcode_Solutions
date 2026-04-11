class Solution:
    def minimumDistance(self, nums):
        from collections import defaultdict
        idx = defaultdict(list)
        for i, v in enumerate(nums):
            idx[v].append(i)
        res = float('inf')
        for positions in idx.values():
            if len(positions) < 3:
                continue
            for t in range(len(positions) - 2):
                i, j, k = positions[t], positions[t+1], positions[t+2]
                res = min(res, 2 * (k - i))
        return res if res != float('inf') else -1