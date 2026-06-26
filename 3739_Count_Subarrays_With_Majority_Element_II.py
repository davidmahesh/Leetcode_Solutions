class Solution:
    def countMajoritySubarrays(self,nums,target):
        n=len(nums)
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+(1 if nums[i]==target else -1)
        vals=sorted(set(pref))
        rank={v:i+1 for i,v in enumerate(vals)}
        sz=len(vals)+1
        bit=[0]*( sz+1)
        def update(i):
            while i<=sz:
                bit[i]+=1
                i+=i&(-i)
        def query(i):
            s=0
            while i>0:
                s+=bit[i]
                i-=i&(-i)
            return s
        ans=0
        for p in pref:
            r=rank[p]
            ans+=query(r-1) if r>1 else 0
            update(r)
        return ans