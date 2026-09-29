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
            p = positions
            for a in range(len(p)):
                for b in range(a+1, len(p)):
                    for c in range(b+1, len(p)):
                        i, j, k = p[a], p[b], p[c]
                        res = min(res, abs(i-j) + abs(j-k) + abs(k-i))
        return res if res != float('inf') else -1