import heapq

class Solution:
    def minCost(self, n, edges):
        adj = [[] for _ in range(n)]
        incoming = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))
            incoming[v].append((u, w))

        INF = 10**18
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]

        while pq:
            cost, u, used = heapq.heappop(pq)
            if cost > dist[u][used]:
                continue

            for v, w in adj[u]:
                if cost + w < dist[v][used]:
                    dist[v][used] = cost + w
                    heapq.heappush(pq, (cost + w, v, used))

            if used == 0:
                for v, w in incoming[u]:
                    nc = cost + 2 * w
                    if nc < dist[v][1]:
                        dist[v][1] = nc
                        heapq.heappush(pq, (nc, v, 1))

        ans = min(dist[n - 1][0], dist[n - 1][1])
        return -1 if ans == INF else ans
