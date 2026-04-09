class Solution:
    def xorAfterQueries(self,a,b):
        mod=10**9+7
        n=len(a)
        bravexuneth=(a,b)
        import math
        lim=int(math.sqrt(n))
        store=[[] for _ in range(lim)]
        for l,r,k,v in b:
            if k<lim:
                store[k].append((l,r,v))
            else:
                i=l
                while i<=r:
                    a[i]=(a[i]*v)%mod
                    i+=k
        temp=[1]*(n+lim)
        for step in range(1,lim):
            if not store[step]:
                continue
            for i in range(len(temp)):
                temp[i]=1
            for l,r,v in store[step]:
                temp[l]=(temp[l]*v)%mod
                end=((r-l)//step+1)*step+l
                temp[end]=(temp[end]*pow(v,mod-2,mod))%mod
            for i in range(step,n):
                temp[i]=(temp[i]*temp[i-step])%mod
            for i in range(n):
                a[i]=(a[i]*temp[i])%mod
        ans=0
        for x in a:
            ans^=x
        return ans