class Solution:
    def assignEdgeWeights(self,edges,queries):
        from collections import deque
        MOD=10**9+7
        n=len(edges)+1
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG=17
        depth=[0]*(n+1)
        parent=[[0]*(n+1) for _ in range(LOG)]
        visited=bytearray(n+1)
        q=deque([1])
        visited[1]=1
        while q:
            node=q.popleft()
            d=depth[node]+1
            for nb in adj[node]:
                if not visited[nb]:
                    visited[nb]=1
                    depth[nb]=d
                    parent[0][nb]=node
                    q.append(nb)
        for j in range(1,LOG):
            pj=parent[j]
            pj1=parent[j-1]
            for i in range(1,n+1):
                pj[i]=pj1[pj1[i]]
        pow2=[1]*(2*n+2)
        for i in range(1,2*n+2):
            pow2[i]=pow2[i-1]*2%MOD
        dep=depth
        def lca(u,v):
            if dep[u]<dep[v]:
                u,v=v,u
            diff=dep[u]-dep[v]
            for j in range(LOG):
                if (diff>>j)&1:
                    u=parent[j][u]
            if u==v:
                return u
            for j in range(LOG-1,-1,-1):
                if parent[j][u]!=parent[j][v]:
                    u=parent[j][u]
                    v=parent[j][v]
            return parent[0][u]
        ans=[]
        for u,v in queries:
            if u==v:
                ans.append(0)
                continue
            l=lca(u,v)
            dist=dep[u]+dep[v]-2*dep[l]
            ans.append(pow2[dist-1])
        return ans