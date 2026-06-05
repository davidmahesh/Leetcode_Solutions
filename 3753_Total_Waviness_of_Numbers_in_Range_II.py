class Solution:
    def totalWaviness(self,num1,num2):
        from functools import lru_cache
        def calc(num):
            s=str(num)
            n=len(s)
            @lru_cache(maxsize=None)
            def dp(pos,tight,prev,prev2,started):
                if pos==n:
                    return (0,1)
                limit=int(s[pos]) if tight else 9
                total_wave=0
                total_count=0
                for d in range(0,limit+1):
                    ntight=tight and d==limit
                    extra=0
                    if not started and d==0:
                        w,c=dp(pos+1,ntight,-1,-1,False)
                    else:
                        nprev2=prev if started else -1
                        nprev=d
                        if started and prev!=-1 and prev2!=-1:
                            if d<prev and prev>prev2:
                                extra=1
                            elif d>prev and prev<prev2:
                                extra=1
                        w,c=dp(pos+1,ntight,nprev,nprev2,True)
                    total_wave+=w+extra*c
                    total_count+=c
                return (total_wave,total_count)
            ans=dp(0,True,-1,-1,False)[0]
            dp.cache_clear()
            return ans
        return calc(num2)-calc(num1-1)