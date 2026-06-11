from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        max_depth = 0
        q = deque([(1, 0, 0)])
        visited = {1}
        while q:
            node, parent, depth = q.popleft()
            max_depth = max(max_depth, depth)
            for nb in graph[node]:
                if nb != parent:
                    visited.add(nb)
                    q.append((nb, node, depth+1))
        return pow(2, max_depth-1, MOD)