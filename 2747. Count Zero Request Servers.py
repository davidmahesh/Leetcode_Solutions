from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        q = sorted((t, i) for i, t in enumerate(queries))

        freq = defaultdict(int)
        ans = [0] * len(queries)
        left = right = active = 0

        for t, idx in q:
            while right < len(logs) and logs[right][1] <= t:
                server = logs[right][0]
                if freq[server] == 0:
                    active += 1
                freq[server] += 1
                right += 1

            while left < right and logs[left][1] < t - x:
                server = logs[left][0]
                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans
