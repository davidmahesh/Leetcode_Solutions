class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        res = float('inf')
        for i in range(len(landStartTime)):
            lend = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                wend = waterStartTime[j] + waterDuration[j]
                t1 = max(lend, waterStartTime[j]) + waterDuration[j]
                t2 = max(wend, landStartTime[i]) + landDuration[i]
                res = min(res, t1, t2)
        return res