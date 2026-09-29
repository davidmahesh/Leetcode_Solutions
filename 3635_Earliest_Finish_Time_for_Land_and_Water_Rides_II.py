from bisect import bisect_left

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        lend = [landStartTime[i]+landDuration[i] for i in range(len(landStartTime))]
        wend = [waterStartTime[j]+waterDuration[j] for j in range(len(waterStartTime))]

        def best_finish(first_ends, second_starts, second_dur, second_ends):
            order = sorted(range(len(second_starts)), key=lambda j: second_starts[j])
            ss = [second_starts[j] for j in order]
            sd = [second_dur[j] for j in order]
            se = [second_ends[j] for j in order]
            m = len(ss)
            pre_min_dur = [0]*m
            suf_min_end = [0]*m
            pre_min_dur[0] = sd[0]
            for k in range(1, m):
                pre_min_dur[k] = min(pre_min_dur[k-1], sd[k])
            suf_min_end[m-1] = se[m-1]
            for k in range(m-2, -1, -1):
                suf_min_end[k] = min(suf_min_end[k+1], se[k])
            res = float('inf')
            for fe in first_ends:
                p = bisect_left(ss, fe)
                if p < m:
                    res = min(res, suf_min_end[p])
                if p > 0:
                    res = min(res, fe + pre_min_dur[p-1])
            return res

        ans = min(
            best_finish(lend, waterStartTime, waterDuration, wend),
            best_finish(wend, landStartTime, landDuration, lend)
        )
        return ans