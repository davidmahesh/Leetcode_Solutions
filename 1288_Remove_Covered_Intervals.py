class Solution:
    def removeCoveredIntervals(self,intervals):
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ans=0
        maxR=0
        for l,r in intervals:
            if r>maxR:
                ans+=1
                maxR=r
        return ans