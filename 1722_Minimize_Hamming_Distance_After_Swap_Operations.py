class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        p = list(range(n))
        def find(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        def union(x, y):
            p[find(x)] = find(y)
        for a, b in allowedSwaps:
            union(a, b)
        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        dist = 0
        for indices in groups.values():
            freq = defaultdict(int)
            for i in indices:
                freq[source[i]] += 1
            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    dist += 1
        return dist