class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        
        def maxReduce(w, t):
            lo, hi = 0, mountainHeight
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if w * mid * (mid + 1) // 2 <= t:
                    lo = mid
                else:
                    hi = mid - 1
            return lo
        
        def canFinish(t):
            total = 0
            for w in workerTimes:
                total += maxReduce(w, t)
                if total >= mountainHeight:
                    return True
            return False
        
        lo = 0
        hi = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        while lo < hi:
            mid = (lo + hi) // 2
            if canFinish(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo