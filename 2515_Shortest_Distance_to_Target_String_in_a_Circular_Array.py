class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        res = float('inf')
        for i, w in enumerate(words):
            if w == target:
                d = abs(i - startIndex)
                res = min(res, d, n - d)
        return res if res != float('inf') else -1