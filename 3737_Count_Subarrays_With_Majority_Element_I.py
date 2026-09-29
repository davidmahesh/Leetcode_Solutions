class Solution:
    def countMajoritySubarrays(self,nums,target):
        n=len(nums)
        ans=0
        for i in range(n):
            cnt=0
            total=0
            for j in range(i,n):
                total+=1
                if nums[j]==target:
                    cnt+=1
                if cnt*2>total:
                    ans+=1
                    
        return ans
