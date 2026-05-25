class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reach = [False]*n
        reach[0] = True
        pre = [0]*n
        pre[0] = 1
        for i in range(1, n):
            pre[i] = pre[i-1] + (1 if reach[i-1] else 0)
        for i in range(1, n):
            if s[i] == '0':
                lo = max(0, i-maxJump)
                hi = i-minJump
                if hi >= 0:
                    window = pre[hi] - (pre[lo-1] if lo > 0 else 0)
                    if window > 0:
                        reach[i] = True
            pre[i] = pre[i-1] + (1 if reach[i] else 0)
        return reach[n-1]