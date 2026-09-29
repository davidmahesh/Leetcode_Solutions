class Solution:
    def arrayRankTransform(self, arr):
        rank = {}
        for i, x in enumerate(sorted(set(arr)), 1):
            rank[x] = i
        return [rank[x] for x in arr]