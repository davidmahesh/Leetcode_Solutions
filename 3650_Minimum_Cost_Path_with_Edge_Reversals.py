import heapq

class Solution:
    def minCost(self, n, edges):
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in adj[u]:
                nc = cost + w
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(pq, (nc, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]
