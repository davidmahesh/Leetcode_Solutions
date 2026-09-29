class Solution:
    def findMaxPathScore(self,edges,online,k):
        from collections import defaultdict,deque
        n=len(online)
        if not edges:
            return -1
        costs=sorted(set(c for _,_,c in edges))
        g_full=defaultdict(list)
        ind_full=[0]*n
        for u,v,c in edges:
            if online[u] and online[v]:
                g_full[u].append(v)
                ind_full[v]+=1
        topo=[]
        ind=ind_full[:]
        q=deque()
        for i in range(n):
            if ind[i]==0 and online[i]:
                q.append(i)
        while q:
            node=q.popleft()
            topo.append(node)
            for nb in g_full[node]:
                ind[nb]-=1
                if ind[nb]==0:
                    q.append(nb)
        adj=defaultdict(list)
        for u,v,c in edges:
            if online[u] and online[v]:
                adj[u].append((v,c))
        def check(mid):
            dp=[float('inf')]*n
            dp[0]=0
            for node in topo:
                if dp[node]==float('inf'):
                    continue
                for nb,c in adj[node]:
                    if c>=mid:
                        nc=dp[node]+c
                        if nc<dp[nb]:
                            dp[nb]=nc
            return dp[n-1]<=k
        lo,hi=0,len(costs)-1
        ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if check(costs[mid]):
                ans=costs[mid]
                lo=mid+1
            else:
                hi=mid-1
        return ans