class Solution:
    def maxTotalValue(self,nums,k):
        import math
        import heapq
        n=len(nums)
        LOG=max(1,int(math.log2(n))+1)
        mx=[[0]*n for _ in range(LOG)]
        mn=[[0]*n for _ in range(LOG)]
        mx[0]=nums[:]
        mn[0]=nums[:]
        for j in range(1,LOG):
            for i in range(n-(1<<j)+1):
                mx[j][i]=max(mx[j-1][i],mx[j-1][i+(1<<(j-1))])
                mn[j][i]=min(mn[j-1][i],mn[j-1][i+(1<<(j-1))])
        def qmax(l,r):
            length=r-l+1
            k=int(math.log2(length))
            return max(mx[k][l],mx[k][r-(1<<k)+1])
        def qmin(l,r):
            length=r-l+1
            k=int(math.log2(length))
            return min(mn[k][l],mn[k][r-(1<<k)+1])
        def val(l,r):
            return qmax(l,r)-qmin(l,r)
        heap=[]
        for l in range(n):
            v=val(l,n-1)
            heapq.heappush(heap,(-v,l,n-1))
        ans=0
        for _ in range(k):
            v,l,r=heapq.heappop(heap)
            ans+=(-v)
            if r>l:
                nv=val(l,r-1)
                heapq.heappush(heap,(-nv,l,r-1))
        return ans