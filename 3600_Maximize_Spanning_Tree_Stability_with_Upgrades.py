class Solution:
    def maxStability(self, n, edges, k):
        must = [(u, v, s) for u, v, s, m in edges if m == 1]
        optional = [(u, v, s) for u, v, s, m in edges if m == 0]

        def feasible(threshold):
            p = list(range(n))
            r = [0] * n

            def find(x):
                while p[x] != x:
                    p[x] = p[p[x]]
                    x = p[x]
                return x

            def union(x, y):
                px, py = find(x), find(y)
                if px == py:
                    return False
                if r[px] < r[py]:
                    px, py = py, px
                p[py] = px
                if r[px] == r[py]:
                    r[px] += 1
                return True

            for u, v, s in must:
                if s < threshold:
                    return False
                if not union(u, v):
                    return False

            no_up = [(u, v, s) for u, v, s in optional if s >= threshold]
            need_up = [(u, v, s) for u, v, s in optional if s < threshold and s * 2 >= threshold]

            for u, v, s in no_up:
                union(u, v)

            upgrades = 0
            for u, v, s in need_up:
                if upgrades < k:
                    if union(u, v):
                        upgrades += 1

            root = find(0)
            return all(find(i) == root for i in range(n))

        candidates = sorted(set(
            val for u, v, s, m in edges
            for val in ([s] if m == 1 else [s, s * 2])
        ))

        if not feasible(candidates[0]):
            return -1

        lo, hi = 0, len(candidates) - 1
        ans = candidates[0]

        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(candidates[mid]):
                ans = candidates[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans