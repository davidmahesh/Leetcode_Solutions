from bisect import bisect_left,bisect_right

class Solution:
    def sumAndMultiply(self, s, queries):
        mod=10**9+7
        pos=[]
        dig=[]
        for i,c in enumerate(s):
            if c!='0':
                pos.append(i)
                dig.append(int(c))

        n=len(pos)
        p10=[1]*(n+1)
        for i in range(1,n+1):
            p10[i]=p10[i-1]*10%mod

        preNum=[0]*(n+1)
        preSum=[0]*(n+1)
        for i in range(n):
            preNum[i+1]=(preNum[i]*10+dig[i])%mod
            preSum[i+1]=preSum[i]+dig[i]

        ans=[]
        for l,r in queries:
            a=bisect_left(pos,l)
            b=bisect_right(pos,r)
            if a==b:
                ans.append(0)
                continue
            x=(preNum[b]-preNum[a]*p10[b-a])%mod
            sm=preSum[b]-preSum[a]
            ans.append(x*sm%mod)

        return ans