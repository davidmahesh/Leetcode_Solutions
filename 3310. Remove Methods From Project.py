from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)

        bad = [False] * n
        stack = [k]
        bad[k] = True

        while stack:
            u = stack.pop()
            for v in g[u]:
                if not bad[v]:
                    bad[v] = True
                    stack.append(v)

        for u, v in invocations:
            if not bad[u] and bad[v]:
                return list(range(n))

        return [i for i in range(n) if not bad[i]]