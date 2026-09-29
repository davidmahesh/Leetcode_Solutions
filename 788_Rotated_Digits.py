class Solution:
    def rotatedDigits(self, n):
        rot = {'0':'0','1':'1','2':'5','5':'2','6':'9','8':'8','9':'6'}
        res = 0
        for x in range(1, n+1):
            s = str(x)
            if any(d not in rot for d in s):
                continue
            r = ''.join(rot[d] for d in s)
            if r != s:
                res += 1
        return res