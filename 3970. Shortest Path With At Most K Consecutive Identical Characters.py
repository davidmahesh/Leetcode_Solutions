import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            cost, u, cnt = heapq.heappop(pq)

            if cost != dist[u][cnt]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:
                next_cnt = cnt + 1 if labels[u] == labels[v] else 1

                if next_cnt <= k and cost + w < dist[v][next_cnt]:
                    dist[v][next_cnt] = cost + w
                    heapq.heappush(pq, (cost + w, v, next_cnt))

        return -1
