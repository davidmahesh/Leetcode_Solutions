class Solution:
    def countCompleteComponents(self, n, edges):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [False] * n
        ans = 0

        for i in range(n):
            if vis[i]:
                continue

            stack = [i]
            vis[i] = True
            nodes = []
            edgeCount = 0

            while stack:
                u = stack.pop()
                nodes.append(u)
                edgeCount += len(g[u])
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        stack.append(v)

            sz = len(nodes)
            edgeCount //= 2
            if edgeCount == sz * (sz - 1) // 2:
                ans += 1

        return ans