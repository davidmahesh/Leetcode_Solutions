from collections import defaultdict, deque

class Solution:
    def minScore(self, n, roads):
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = set()
        q = deque([1])
        visited.add(1)
        res = float('inf')

        while q:
            node = q.popleft()
            for nb, d in graph[node]:
                res = min(res, d)
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)

        return res